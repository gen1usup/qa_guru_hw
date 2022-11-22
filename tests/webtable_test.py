import allure
from selene import have
from selene.support.shared import browser
from mimesis import Person
from mimesis.locales import Locale

def set_user_info():
    person = Person(Locale.RU)
    user_info = []
    user_info.append(person.first_name())
    user_info.append(person.last_name())
    user_info.append(person.email())
    user_info.append(str(person.age()))
    user_info.append(str(person.weight(1000, 10000)))
    user_info.append("department")
    return user_info

@allure.label("owner", "dlebedev")
@allure.feature("webtables")
@allure.story("Проверка добавления существующей записи")
def test_table_add(selenoid_with_video):
    browser.open('/webtables')
    browser.element('#addNewRecordButton').click()
    registration_form_fields = browser.elements('.mr-sm-2')
    user_info = set_user_info()
    for i in range(6):
        registration_form_fields[i].type(user_info[i])
    browser.element('#submit').click()
    # new_element = browser.all("//*[@class='rt-tbody']/div[4]/div/div")
    browser.element("//*[@class='rt-tbody']/div[4]/div").should(have.text(
        f'{user_info[0]}\n{user_info[1]}\n{user_info[3]}\n{user_info[2]}\n{user_info[4]}\n{user_info[5]}'))
    # new_line_elements = []
    # for i in range(6):
    #     new_line_elements.append(new_element[i]().text)
    # assert set(new_line_elements) == set(user_info)

@allure.label("owner", "dlebedev")
@allure.feature("webtables")
@allure.story("Проверка удаления существующей записи")
def test_table_delete(selenoid_with_video):
    browser.open('/webtables')
    begin_count = len(browser.elements('.action-buttons'))
    browser.element('#delete-record-3').click()
    browser.elements('.action-buttons').should(have.size(begin_count - 1))

@allure.label("owner", "dlebedev")
@allure.feature("webtables")
@allure.story("Проверка изменения существующей записи")
def test_change(selenoid_with_video):
    browser.open('/webtables')
    user_info = set_user_info()
    browser.element('#edit-record-2').click()
    registration_form_fields = browser.elements('.mr-sm-2')
    for i in range(6):
        registration_form_fields[i].clear().type(user_info[i])
    browser.element('#submit').click()
    browser.element("//*[@class='rt-tbody']/div[2]/div").should(have.text(
        f'{user_info[0]}\n{user_info[1]}\n{user_info[3]}\n{user_info[2]}\n{user_info[4]}\n{user_info[5]}'))
    # new_line_elements = []
    # for i in range(6):
    #     new_line_elements.append(new_element[i]().text)
    # assert set(new_line_elements) == set(user_info)

