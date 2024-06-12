import time
import pytest
from pageobject.login import Loginpage
from Utilities.logger import logclass
from pageobject.Dashbord import Dashbo
import configparser
config=configparser.ConfigParser()
config.read("Utilities/inpout.properties")
@pytest.mark.usefixtures("setup")
class Test_login(logclass):
    def test_001(self):
        log= self.getthelogs()

        lg=Loginpage(self.driver)
        ds=Dashbo(self.driver)
        time.sleep(10)
        log.info("test case Start")
        lg.logi(config.get("credential","user_id"))

        time.sleep(5)
        lg.password(config.get("credential","user_password"))
        log.info("user password enter a sucessfully")
        time.sleep(5)
        lg.click()
        log.info("Login Button Click sucessfully")
        log.info("login Sucessfully")
        time.sleep(3)
        ds.admin()
        log.info("admin click sucessfully")
        time.sleep(5)
        ds.user_add()
        log.info("click sucessfully in add user")
        time.sleep(5)
        ds.user_role()
        log.info("user role click sucessfully")
        time.sleep(3)
        ds.ess()
        log.log("click sucessfully in ess")
        time.sleep(10)








    # def test_002(self):
    #     log = self.getthelogs()
    #     lg=Loginpage(self.driver)
    #     log.info("log start")
    #     time.sleep(10)
    #     lg.invalid_login(config.get("credential","invalid_id"))
    #     log.info("Enter A invalid usernmae sucessfully")
    #     time.sleep(5)
    #     lg.invalid_pass(config.get("credential","invalid_password"))
    #     log.info("user password enter a sucessfully")
    #     time.sleep(5)
    #     lg.clic()
    #     log.info(" fail the login sucessfully")
    #     time.sleep(5)
    #     lg.invaid_cr()
    #     log.info("message Show sucessfully")
    #     time.sleep(5)



