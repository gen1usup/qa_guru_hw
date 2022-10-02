import time

from mimesis import Person
from mimesis.enums import Locale
from selene.support.shared import browser
from selene import be, command

def set_user_info():
    person = Person(Locale.RU)
    user_info = {}

    user_info['first_name'] = person.first_name()
    user_info['last_name'] = person.last_name()
    user_info['email'] = person.email()
    user_info['gender'] = 'Male'
    user_info['mobile'] = str(person.telephone(mask='##########'))
    user_info['birthDate'] = '12 August,1994'
    user_info['address'] = person.get_current_locale()
    user_info['empty'] = ''
    user_info['full_name'] = user_info.get('first_name') + ' ' + user_info.get('last_name')
    return user_info


def test_form(open_browser):
    user_info = set_user_info()
    browser.open('/automation-practice-form')
    browser.element('footer').perform(command.js.set_style_visibility_to_hidden)
    browser.element('[id="firstName"]').type(user_info.get('first_name'))
    browser.element('[id="lastName"]').type(user_info.get('last_name'))
    browser.element('#userEmail').type(user_info.get('email'))
    browser.element(f'//*[contains(text(),"{user_info.get("gender")}")]').click()
    browser.element('[id="userNumber"]').type(user_info.get('mobile'))
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('//*[@value=1994]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('//*[text()="August"]').click()
    browser.element("//*[contains(@class, 'react-datepicker__day--012') and contains(@aria-label,'August')]").click()
    browser.element('[id="submit"]').click()

    browser.element(".modal-content").should(be.visible)
    total_page = browser.elements("//*[@class='table-responsive']/table/tbody/tr/td[2]")
    for element in total_page:
        if element().text in user_info.values():
            continue
        else:
            assert False











