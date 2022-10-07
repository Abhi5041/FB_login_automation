import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='class')
def setup(request):
    obj = Service("/Users/singh/Downloads/geckodriver-v0.31.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=obj)
    driver.maximize_window()
    driver.get("https://en-gb.facebook.com/")
    request.cls.driver= driver
    yield
    driver.close()