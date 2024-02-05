import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

#importa o confitest e declara driver dentro dos testes c1,c2,c3


driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    #setup
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield            # run test


    #teardown
    driver.quit()