import pytest
import json
from requests import options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Static values
mid_screen = [1440, 900]
valid_browsers = ['firefox', 'safari', 'chrome']
valid_envs = ['dev', 'stage']

# Default values
default_browser = 'firefox'
default_env = 'stage'

def pytest_addoption(parser):
    # action="store" stores value in a variable of the same name as the option
    parser.addoption("--browser", action="store", default="", choices=("firefox", "safari", "chrome"), help="Browser name, options are: 'firefox', 'safari', 'chrome'. Default is firefox")
    parser.addoption("--env", action="store", default="", choices=("dev", "stage"), help="Test environment name, options are: 'dev', 'stage'. Default is dev")

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

    cli_browser = request.config.getoption("--browser")
    cli_env = request.config.getoption("--env")
    
    with open(r"config.json") as config_file:
        config = json.load(config_file)

    # Start with defaults
    tgt_browser = default_browser
    tgt_env = default_env

    if cli_browser != '':
        tgt_browser = cli_browser # CLI parser setup above ensures valid value
    elif 'test-browser' in config and config['test-browser'].lower() in valid_browsers:
        tgt_browser = config['test-browser'].lower()
    
    if cli_env != '':
        tgt_env = cli_env # CLI parser setup above ensures valid value
    elif 'test-env' in config and config['test-env'].lower() in valid_envs:
        tgt_env = config['test-env'].lower()
    
    config['test-browser'] = tgt_browser
    config['test-env'] = tgt_env

    print('Browser: ', config['test-browser'])
    print('Env: ', config['test-env'])
    print('Exiting conftest.py config()')
    return config

@pytest.fixture(scope='class')
def domain(config):
    print('\n*********** Entering conftest.py domain()')

    if config['test-env'] == 'dev':
        url = config['domain-dev']
    else:
        url = config['domain-stage']

    print('\n*********** Domain: ', url)
    print('\n*********** Exiting conftest.py domain()')
    return url

@pytest.fixture(scope='session')
def driver(config):
    print('\n*********** Entering conftest.py driver()')
    desiredBrowser = config['test-browser']

    if desiredBrowser == 'firefox':
        firefoxOpts = webdriver.FirefoxOptions()
        firefoxOpts.add_argument('--no-sandbox')

        ff_service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=ff_service, options=firefoxOpts)

        
        #b = webdriver.Firefox(GeckoDriverManager().install())
    elif desiredBrowser == 'safari':
        driver = webdriver.Safari()
    elif desiredBrowser == 'chrome':
        #driver_path = ChromeDriverManager().install()
        #chromeOpts = webdriver.ChromeOptions()
        #chromeOpts.add_argument('--no-sandbox')

        #chrome_service = Service(ChromeDriverManager().install())
        #chrome_service = Service(executable_path=ChromeDriverManager().install())
        #b = webdriver.Chrome(service=chrome_service, options=chromeOpts)
        #b = webdriver.Chrome(executable_path=driver_path, options=chromeOpts)
        driver = webdriver.Chrome()
    
    driver.set_window_size(mid_screen[0], mid_screen[1])
    yield driver
    driver.close() # Closes currenly open window, leaves others open, execution process of driver remains active
    # b .quit() # Closes all open windows, terminates execution process of driver
    print('Exiting conftest.py driver()')