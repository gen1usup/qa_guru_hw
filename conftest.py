import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.environ['GH_TOKEN'] = "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 "

@pytest.fixture()
def open_browser():
    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['acceptInsecureCerts'] = True
    caps['acceptSslCerts'] = True
    # driver = webdriver.Chrome(desired_capabilities=caps)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    browser.config.driver = webdriver.Chrome(options=options, desired_capabilities=caps)

    # browser.config.browser_name = 'firefox'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.close_current_tab()





    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # options.add_argument('--ignore-certificate-errors-spki-list')
    # browser.config.driver = webdriver.Chrome("E:\drivers\chromedriver_win32\chromedriver.exe", chrome_options=options)
