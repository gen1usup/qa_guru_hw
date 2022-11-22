import allure
from selene import have, command
from selene.support.shared import browser

from demoqa.pages.automation_practice_form import set_fullname, set_email, set_phone, \
    select_gender, set_subjects, select_hobbies, upload_picture, check_fill_form, submit_form, set_address, \
    set_birth_date_by_type, open_page, set_birth_date_by_click
from demoqa.utils import attach
from tests.testdata.users import random_user

def given_opened_form():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)

@allure.label("owner", "dlebedev")
@allure.feature("automation-practice-form")
@allure.story("e2e тест заполнения")
def test_form(selenoid_with_video):
    user_info = random_user

    open_page()
    given_opened_form()
    set_fullname(user_info.first_name, user_info.last_name)
    set_email(user_info.email)
    select_gender(user_info.gender)
    set_phone(user_info.mobile)
    set_birth_date_by_click(user_info.birth_day, user_info.birth_month, user_info.birth_year)
    # set_birth_date_by_type(user_info.birth_day, user_info.birth_month, user_info.birth_year)
    set_subjects(user_info.subjects)
    select_hobbies(user_info.hobbies)
    upload_picture(user_info.name_jpg)
    set_address(user_info.address)
    submit_form()

    check_fill_form(user_info)
