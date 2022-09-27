import os
import pytest
from selene.support.shared import browser

os.environ['GH_TOKEN'] = "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 "

@pytest.fixture()
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.close_current_tab()




