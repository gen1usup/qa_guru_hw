import time

from selene import have, be
from selene.support.shared import browser
from mimesis import Person
from mimesis.locales import Locale

# def get_same_name():
#     return str(int(time.time()))

def set_user_info():
    person = Person(Locale.RU)
    user_info = []
    user_info.append(person.first_name())
    user_info.append(person.last_name())
    user_info.append(person.email())
    user_info.append(person.age())
    user_info.append(person.weight(1000,10000))
    user_info.append(person.university())
    return user_info


def test_table_add(open_browser):
    browser.open('/webtables')
    browser.element('#addNewRecordButton').click()
    registration_form_fields = browser.elements('.mr-sm-2')
    user_info = set_user_info()
    for i in range(6):
        registration_form_fields[i].type(user_info[i])
    browser.element('#submit').click()
    new_element = browser.elements("//*[@class='rt-tbody']/div[4]/div/div")
    for i in range(2):
        new_element[i].should(have.text(user_info[i]))

def test_table_delete(open_browser):
    browser.open('/webtables')
    browser.element('#delete-record-3').click()

def test_change(open_browser):
    browser.open('/webtables')
    user_info = set_user_info()
    browser.element('#edit-record-2').click()
    registration_form_fields = browser.elements('.mr-sm-2')
    for i in range(6):
        registration_form_fields[i].clear().type(user_info[i])
    browser.element('#submit').click()
    new_element = browser.elements("//*[@class='rt-tbody']/div[2]/div/div")
    for i in range(2):
        new_element[i].should(have.text(user_info[i]))

