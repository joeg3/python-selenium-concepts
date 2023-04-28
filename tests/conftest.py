import pytest
import json
from requests import options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Static values
mid_screen = [1440, 900]
VALID_BROWSERS = ['firefox', 'safari', 'chrome']
VALID_ENVS = ['dev', 'stage']

# Default values
DEFAULT_BROWSER = 'chrome'
DEFAULT_ENV = 'stage'

def pytest_addoption(parser):
    """ Define CLI options """
    # action="store" stores value in a variable of the same name as the option
    parser.addoption("--browser", action="store", default="", choices=("firefox", "safari", "chrome"), help="Browser name, options are: 'firefox', 'safari', 'chrome'. Default is firefox")
    parser.addoption("--env", action="store", default="", choices=("dev", "stage"), help="Test environment name, options are: 'dev', 'stage'. Default is dev")

@pytest.fixture(scope='session')
def config(request):
    """ From CLI args, config.json, and defaults, determine browser driver and environment to be used in tests """
    cli_browser = request.config.getoption("--browser")
    cli_env = request.config.getoption("--env")
    
    with open(r"config.json") as config_file:
        config = json.load(config_file)
    
    config['test-browser'] = determine_config_value(cli_browser, 'test-browser', config, VALID_BROWSERS, DEFAULT_BROWSER)
    config['test-env'] = determine_config_value(cli_env, 'test-ENV', config, VALID_ENVS, DEFAULT_ENV)

    print("\n\n========================== TEST INPUTS ============================")
    print(f"Using '{config['test-browser']}' browser for testing")
    print(f"Using '{config['test-env']}' environment for testing")
    print('Exiting conftest.py config()\n\n')
    return config

@pytest.fixture(scope='session')
def domain(config):
    """ Depending on environment (dev or stage), return domain base url """
    if config['test-env'] == 'dev':
        url = config['domain-dev']
    else:
        url = config['domain-stage']

    print('\n*********** Domain: ', url)
    return url

@pytest.fixture(scope='session')
def driver_for_script(config):
    """ This fixture is for use with test scripts, not test classes """
    desiredBrowser = config['test-browser']
    driver = get_driver(desiredBrowser)
    yield driver
    #driver.close() # Closes currenly open window, leaves others open, execution process of driver remains active
    # b .quit() # Closes all open windows, terminates execution process of driver

@pytest.fixture(scope='function')
def tear_down(driver):
    yield
    driver.close()
    #return driver

@pytest.fixture(scope='session')
def test_data(config):
    """ Depending on environment (dev or stage), return test data """
    env = config['test-env']
    file = f"testdata/{env}_test_data.json"
    with open(file, "r") as test_data_file:
        test_data = json.load(test_data_file)
    return test_data

@pytest.fixture(scope='class')
def domain_for_class(request, config):
    """ Depending on environment (dev or stage), return domain base url """
    """ This fixture is for use with test classes, not test scripts """
    if config['test-env'] == 'dev':
        url = config['domain-dev']
    else:
        url = config['domain-stage']

    request.cls.domain_c = url
    print('\n*********** Domain: ', url)
    return url

# When using classes for test cases that define fixutures at the class level, you can't pass a value from the fixture to the test
# with yield. So we instead set a class variable in the fixture.
#@pytest.fixture(params=["chrome", firefox"], scope='class') in fixuture you would check browser and create driver for specific browser
@pytest.fixture(scope='class')
def driver_for_class(request, config):
    """ This fixture is for use with test classes, not test scripts """
    desiredBrowser = config['test-browser']
    web_driver = get_driver(desiredBrowser)
    request.cls.driver_cls = web_driver # This sets class varible driver
    yield
    web_driver.close() # Closes currenly open window, leaves others open, execution process of driver remains active
    # b .quit() # Closes all open windows, terminates execution process of driver











######################### Locator fixtures #############################
@pytest.fixture(scope='class')
def locator_test_domain1(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator1-dev']
    else:
        url = config['domain-locator1-stage']

    print('\n*********** Locator 1 Domain: ', url)
    return url

@pytest.fixture(scope='class')
def locator_test_domain2(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator2-dev']
    else:
        url = config['domain-locator2-stage']

    print('\n*********** Locator 2 Domain: ', url)
    return url

@pytest.fixture(scope='class')
def locator_test_domain3(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator3-dev']
    else:
        url = config['domain-locator3-stage']

    print('\n*********** Locator 3 Domain: ', url)
    return url

@pytest.fixture(scope='class')
def locator_test_domain4(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator4-dev']
    else:
        url = config['domain-locator4-stage']

    print('\n*********** Locator 4 Domain: ', url)
    return url

@pytest.fixture(scope='class')
def locator_test_domain5(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator5-dev']
    else:
        url = config['domain-locator5-stage']

    print('\n*********** Locator 5 Domain: ', url)
    return url

@pytest.fixture(scope='class')
def locator_test_domain6(config):

    if config['test-env'] == 'dev':
        url = config['domain-locator6-dev']
    else:
        url = config['domain-locator6-stage']

    print('\n*********** Locator 6 Domain: ', url)
    return url

def get_driver(browser):
    # In Windows, I think instead of specifying the path, you can put the drivers in C:\Users\<name>\AppData\Local\Programs\Python\Python39\Scripts
    # On Mac, I think it works without specifying the path because I put the driver in /usr/local/bin which is on my $PATH

    if browser == 'firefox':
        firefoxOpts = webdriver.FirefoxOptions()
        firefoxOpts.add_argument('--no-sandbox')
        ff_service = FirefoxService(GeckoDriverManager().install()) # OR Service('/usr/local/bin/geckodriver')
        driver = webdriver.Firefox(service=ff_service, options=firefoxOpts)
        #driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser == 'safari':
        driver = webdriver.Safari()
    elif browser == 'chrome':
        driver = webdriver.Chrome() # I think this works because I have the chrome driver on my $PATH
        # Another way:
        # chrome_service = ChromeService('/usr/local/bin/chromedriver')
        # driver = webdriver.Chrome(service=chrome_service)
        # Might also see the following, which was deprecated in Selenium 4
        # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    elif browser == 'edge':
        edge_service = EdgeService(executable_path='/usr/local/bin/msedgedriver')
        driver = webdriver.Edge(service=edge_service)
    else:
        driver = webdriver.Chrome()

    driver.set_window_size(mid_screen[0], mid_screen[1])
    return driver

@pytest.fixture()
def ytdriver():
    driver = webdriver.Chrome()
    return driver

def determine_config_value(cli_value, config_key, config_values, valid_values, default_value):
    """ Determine config value to use. """
    """ Command line has precedence over values from config file, which has precedence over default values """
    """ pytest_addoption() fixture and default values constants ensure valid values, so only verify values from config file """
    if cli_value:
        return cli_value
    elif config_key in config_values:
        if config_values[config_key].lower() in valid_values:
            return config_values[config_key].lower()
        else:
            pytest.fail(f"Invalid value in config.json. Is: '{config_values[config_key]}', but should be: {valid_values}")
    else:
        return default_value
