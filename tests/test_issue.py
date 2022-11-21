import allure
import pytest
from selene import by, be
from selene.support.shared import browser
from allure_commons.types import Severity

@pytest.fixture(scope='module')
def full_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dslebedev")
@allure.feature("Allure HW")
@allure.story("Просто тест")
@allure.link("https://github.com", name="Testing")
def test_clear_selene(full_size):
    browser.open("https://github.com")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dlebedev")
@allure.feature("Allure HW")
@allure.story("Тест с with allure step")
@allure.link("https://github.com", name="Testing")
def test_with_lambda(full_size):
    with allure.step("Открытие главной страницы"):
        browser.open("https://github.com")
    with allure.step("Поиск репозитория"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()
    with allure.step("Переход по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открытие вкладки Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверка наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dlebedev")
@allure.feature("Allure HW")
@allure.story("Тест с декоратором")
@allure.link("https://github.com", name="Testing")
def test_with_decorator(full_size):
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открытие главной страницы")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step("Переход по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открытие вкладки Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверка наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()



