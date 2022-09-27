import time

from selene.support.shared import browser
from selene import be, command


def table_add_delete_change_test(open_browser):
    browser.open('/webtables')
    print(time.gmtime())