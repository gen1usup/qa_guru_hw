import datetime

from selene import command, have, be
from selene.support.shared import browser

def open_page():
    browser.open('/automation-practice-form')
    hide_footer()

def hide_footer():
    browser.element('footer').perform(command.js.set_style_visibility_to_hidden)


def set_fullname(first_name, last_name):
    browser.element('[id="firstName"]').type(first_name)
    browser.element('[id="lastName"]').type(last_name)


def set_email(email):
    browser.element('#userEmail').type(email)


def select_gender(gender):
    browser.element(f'//*[contains(text(),"{gender}")]').click()


def set_phone(number):
    browser.element('[id="userNumber"]').type(number)


def set_subjects(subjects):
    for subj in subjects:
        browser.element('#subjectsInput').type(subj).press_tab()


def select_hobbies(hobbies):
    for hobby in hobbies:
        browser.element(f'//*[contains(text(),"{hobby}")]').click()


def upload_picture(jpg):
    browser.element('#uploadPicture').send_keys(jpg)


def set_birth_date_by_click(day, month, year):
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').type(year).click()
    browser.element('.react-datepicker__month-select').type(month).click()
    browser.element(
        f"//*[contains(@class, 'react-datepicker__day--0"
        f"{day}') and contains(@aria-label,'"
        f"{month}')]").click()


def set_birth_date_by_type(day, month, year):
    date = datetime.datetime.strptime(f'{day} {month} {year}', '%d %B %Y')
    browser.element('[id="userNumber"]').press_tab()
    browser.element('#dateOfBirthInput').double_click().double_click().set_value(date.strftime('%d %b %Y')).press_enter()


def set_address(address):
    browser.element('#currentAddress').type(address)


def submit_form():
    browser.element('[id="submit"]').click()


def check_fill_form(user_info):
    data = [
        ('Student Name', f'{user_info.first_name} {user_info.last_name}'),
        ('Student Emai', user_info.email),
        ('Gender', user_info.gender),
        ('Mobile', user_info.mobile),
        ('Date of Birth', f'{user_info.birth_day} {user_info.birth_month},{user_info.birth_year}'),
        ('Subjects', ", ".join(user_info.subjects)),
        ('Hobbies', ", ".join(user_info.hobbies)),
        ('Picture', user_info.name_jpg),
        ('Address', user_info.address)
    ]
    model_content = browser.elements("tbody tr")
    browser.element(".modal-content").should(be.visible)
    for element, user_data in data:
        # assert model_content.element_by(have.text(element)).all('td')[1].should(have.text(user_data))
        # model_content.all(f"//*[contains(text(),'{element}')]")[0].element('./td[2]').should(have.text(user_data))
        model_content.element_by(have.text(element)).element('./td[2]').should(have.text(user_data))
