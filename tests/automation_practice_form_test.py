from selene.support.shared import browser
from demoqa.pages.automation_practice_form import hide_footer, set_fullname, set_email, set_phone, \
    select_gender, set_subjects, select_hobbies, upload_picture, check_fill_form, submit_form, set_address, \
    set_birth_date_by_click, set_birth_date_by_type, open_page
from tests.testdata.users import random_user


def test_form(open_browser):

    user_info = random_user

    open_page()
    set_fullname(user_info.first_name, user_info.last_name)
    set_email(user_info.email)
    select_gender(user_info.gender)
    set_phone(user_info.mobile)
    set_birth_date_by_click(user_info.birth_day, user_info.birth_month, user_info.birth_year)
    # set_birth_date_by_type(user_info.birth_day, user_info.birth_month, user_info.birth_year)
    set_subjects(user_info.subjects)
    select_hobbies(user_info.hobbies)
    upload_picture(user_info.jpg)
    set_address(user_info.address)
    submit_form()

    check_fill_form(user_info)



