import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser
config=configparser.ConfigParser()
config.read("Utilities/inpout.properties")
@pytest.fixture
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(options=options)
    request.cls.driver.maximize_window()
    request.cls.driver.get(config.get("url","base_url"))
    yield
    request.cls.driver.quit()


