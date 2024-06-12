from selenium.webdriver.common.by import By
class Dashbo:
    def __init__(self,driver):
        self.driver=driver
    admin_click_xpath="//li[1]//a[1]//span[1]"
    adduser_xpath="//button[normalize-space()='Add']"
    user_role_xpath="//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    ess_select_xpath="//div[contains(text(),'ESS')]"


    def admin(self):
        self.driver.find_element(By.XPATH,self.admin_click_xpath).click()
    def user_add(self):
        self.driver.find_element(By.XPATH,self.adduser_xpath).click()
    def user_role(self):
        self.driver.find_element(By.XPATH,self.user_role_xpath).click()
    def ess(self):
        self.driver.find_element(By.XPATH,self.ess_select_xpath).click()
