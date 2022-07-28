from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import upload_file_to_cyops
import os
import arrow
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = get_logger('web_scraper')

def url_parser(params):
    url = params.get('url')
    if not url.startswith('https://') and not url.startswith('http://'):
        return 'https://' + url
    else:
        return url

def handle_upload_file_to_cyops(file_path):
    try:
        file_name = os.path.basename(file_path)
        attach_response = upload_file_to_cyops(file_path=file_path,
                                               filename=file_name,
                                               name=file_name,
                                               create_attachment=True)
        logger.debug('{0}'.format(str(type(attach_response))))
        os.remove(file_path)
        return {'file_details':attach_response}
    except Exception as err:
        os.remove(file_path)
        logger.exception('An exception occurred {0}'.format(str(err)))
        raise ConnectorError('An exception occurred {0}'.format(str(err)))

def selenium_init():
    try:    
        connector_dir = os.path.dirname(os.path.realpath(__file__))
        chromedriver_path = connector_dir + "/chromedriver"        
        options = Options()
        options.binary_location = "/opt/google/chrome/google-chrome"
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1024x768')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    except Exception as exp:
        logger.exception('Error Initiating WebDriver {}'.format(exp))
        raise ConnectorError('Error Initiating WebDriver {}'.format(exp))    
    
def get_web_page_source(config, params):
    try:
        url = url_parser(params)
        driver = selenium_init()
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        return page_source

    except Exception as exp:
        logger.exception('Error Getting URL Content: {}'.format(exp))
        raise ConnectorError('Error Getting URL Content: {}'.format(exp))

def get_screenshot(config, params):
    try:
        url = url_parser(params)
        filename = urlparse(url).netloc
        driver = selenium_init()
        file_path = '/tmp/{0}_{1}.png'.format(filename,arrow.get().int_timestamp)
        driver.get(url)
        driver.save_screenshot(file_path)
        driver.quit()
        return handle_upload_file_to_cyops(file_path)
        
    except Exception as exp:
        logger.exception('Error Taking a Screenshot: {}'.format(exp))
        raise ConnectorError('Error Taking a Screenshot: {}'.format(exp))

def _check_health(config):
    if not os.path.exists('/opt/google/chrome/google-chrome'):
        logger.exception('Error Initiating Web Driver')
        raise ConnectorError('Error Initiating Web Driver')


operations = {
    'get_web_page_source': get_web_page_source,
    'get_screenshot': get_screenshot
}