from selenium.webdriver.common.by import By


class LoginFB:

    user_id = (By.CSS_SELECTOR,"input[class='inputtext _55r1 _6luy']")
    Password = (By.CSS_SELECTOR,"input[class='inputtext _55r1 _6luy _9npi']")
    submit_btn = (By.CSS_SELECTOR,"button[class = '_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
    validate = (By.XPATH,"//*[text()='Abhinandan Singh']")

    def __init__(self,driver):
        self.driver = driver

    def enter_user_id(self):
        return self.driver.find_element(*LoginFB.user_id)

    def enter_password(self):
        return self.driver.find_element(*LoginFB.Password)

    def press_enter(self):
        return self.driver.find_element(*LoginFB.submit_btn)

    def validating(self):
        return self.driver.find_element(*LoginFB.validate)
