import pytest
from selenium.webdriver.common.by import By
from Baseclass import BaseClass
from Logincredential import LoginFB


class Testone(BaseClass):

    def test_end2end(self, getdata):
        log = self.getlogger()

        loginpage_obj =LoginFB(self.driver)
        log.info("login page object is created")

        loginpage_obj.enter_user_id().send_keys(getdata[0])
        log.info("Wser ID entered + " + getdata[0])
        loginpage_obj.enter_password().send_keys(getdata[1])
        log.info("is password correct "+"******")

        loginpage_obj.press_enter().click()
        log.info(" successfully submitted !! Welcome to Facebook home page")

        text_test = loginpage_obj.validating().text
        print(text_test)
        assert text_test == 'Abhinandan Singh'
        log.info("validation  successfull")

    @pytest.fixture(params=[("9452087226","Singh@05")])
    def getdata(self, request):
        return request.param

