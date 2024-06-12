from selenium.webdriver.common.by import By
class Loginpage:
    def __init__(self,driver):
        self.driver=driver
    userid_xpath = "//input[@placeholder='Username']"
    password_xpath = "//input[@placeholder='Password']"
    login_xath = "//button[@type='submit']"
    invalid_credi="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    def logi(self,user):
        self.driver.find_element(By.XPATH,self.userid_xpath).send_keys(user)
    def password(self,passwordq):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(passwordq)
    def click(self):
        self.driver.find_element(By.XPATH,self.login_xath).click()
    def invalid_login(self,invalidlog):
        self.driver.find_element(By.XPATH,self.userid_xpath).send_keys(invalidlog)
    def invalid_pass(self,invalidpassword):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(invalidpassword)
    def clic(self):
        self.driver.find_element(By.XPATH,self.login_xath).click()
    def invaid_cr(self):
        if 'Invalid credentials'in self.driver.find_element(By.XPATH,self.invalid_credi).text:
            assert True
        else:
            assert False
