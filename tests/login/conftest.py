import time

import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope='function')
def press_login_button(user_login_fixture):
    user_login_fixture.login_page()
    time.sleep(10)

    yield user_login_fixture


@pytest.fixture(params=["qa.random.app.122automation@gmail.com", "qa.random.app.automation@gmail.com"],
                ids=["InCorrectLogin", "CorrectLogin"])
def mail(request):
    exp_res = False if request.param == "qa.random.app.122automation@gmail.com" else True
    yield request.param, exp_res


@pytest.fixture(params=["qa_automation_password123", "qa_automation_password"], ids=["InCorrectPass", "CorrectPass"])
def password(request):
    exp_res = False if request.param == "qa_automation_password123" else True
    yield request.param, exp_res


