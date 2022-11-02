import pytest
import json
from requests import options

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Static values
mid_screen = [1440, 900]
valid_browser = ['firefox', 'safari']
valid_env = ['dev', 'stage']

# Default values
default_browser = 'firefox'
default_env = 'stage'

def pytest_addoption(parser):
    # action="store" stores value in a variable of the same name as the option
    parser.addoption("--browser", action="store", default="firefox", choices=("firefox", "safari"), help="Browser name, options are: 'firefox', 'safari'. Default is firefox")
    parser.addoption("--env", action="store", default="", help="Test environment name, options are: 'dev', 'stage'. Default is dev")

@pytest.fixture
def setup(request):
    print('\n*********** Entering conftest.py setup()')
    # Launch browser and open website, testcases run during yeild, then close browser
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('http://www.google.com')
    driver.maximize_window()
    request.cls.driver = driver # Any test class (cls) using this fixture can reference the driver that we setup here in the fixture.
    yield
    driver.close()

@pytest.fixture(scope='session')
def config(request):
    print('\n*********** Entering conftest.py config()')
    print('\n*** Values auto stored from cmd line ***')
    #print('browser: ', browser)

    cli_browser = request.config.getoption("--browser")
    cli_env = request.config.getoption("--env")

    print('********** cli_browser', cli_browser)
    print('********** cli_env', cli_env)
    #print("))))))))))))))))))))value of env", env)

    # Start with defaults
    tgt_browser = 'firefox'
    tgt_env = default_env

    with open(r"config.json") as config_file:
        config = json.load(config_file)


    if 'test_browser' in config:
        tgt_browser = config['test_browser'].lower()
    if 'test_env' in config:
        tgt_env = config['test_env'].lower()
    
    if tgt_browser in valid_browser:
        config['test-browser'] = tgt_browser

    if tgt_env in valid_env:
        config['test-env'] = tgt_env

    print('Browser: ', config['test-browser'])
    print('Env: ', config['test-env'])
    print('Exiting conftest.py config()')
    return config

@pytest.fixture(scope='class')
def domain(config):
    print('\n*********** Entering conftest.py domain()')
    desiredEnv = config['test-env']

    if desiredEnv == 'dev':
        u = config['domain-dev']
    else:
        u = config['domain-stage']

    print('\n*********** Domain: ', u)
    print('\n*********** Exiting conftest.py domain()')
    return u

@pytest.fixture(scope='session')
def driver(config):
    print('\n*********** Entering conftest.py driver()')
    desiredBrowser = config['test-browser']

    if desiredBrowser == 'firefox':
        firefoxOpts = webdriver.FirefoxOptions()
        firefoxOpts.add_argument('--no-sandbox')

        service = FirefoxService(GeckoDriverManager().install())
        b = webdriver.Firefox(service=service, options=firefoxOpts)

        
        #b = webdriver.Firefox(GeckoDriverManager().install())
    elif desiredBrowser == 'safari':
        b = webdriver.Safari()
    
    b.set_window_size(mid_screen[0], mid_screen[1])
    yield b
    b.close() # Closes currenly open window, leaves others open, execution process of driver remains active
    # b .quit() # Closes all open windows, terminates execution process of driver
    print('Exiting conftest.py driver()')