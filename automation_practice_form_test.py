from selene.support.shared import browser
from selene import be, command


def test_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('footer').perform(command.js.set_style_visibility_to_hidden)
    browser.element('[id="firstName"]').type('selene')
    browser.element('[id="lastName"]').type('selene1')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('[id="userNumber"]').type('1234567890')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('//*[@value=1994]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('//*[text()="September"]').click()
    browser.element("//*[contains(@class, 'react-datepicker__day--030') and contains(@aria-label,'September')]").click()
    browser.element('[id="submit"]').click()
    browser.element(".modal-content").should(be.visible)

    # document.querySelector("footer").style.visibility = 'hidden'





