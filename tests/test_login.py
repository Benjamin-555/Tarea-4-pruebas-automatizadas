import time
from selenium.webdriver.common.by import By
from driver_factory import get_driver, screenshot

URL = "https://www.saucedemo.com/"


def login(driver, user, password):
    driver.get(URL)
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


def test_login_exitoso():
    driver = get_driver()
    try:
        login(driver, "standard_user", "secret_sauce")
        assert "inventory" in driver.current_url
        screenshot(driver, "login_exitoso")
    finally:
        driver.quit()


def test_login_incorrecto():
    driver = get_driver()
    try:
        login(driver, "wrong_user", "wrong_password")
        error = driver.find_element(By.CSS_SELECTOR, "h3").text.lower()
        assert "epic sadface" in error
        screenshot(driver, "login_incorrecto")
    finally:
        driver.quit()


def test_login_vacio():
    driver = get_driver()
    try:
        login(driver, "", "")
        error = driver.find_element(By.CSS_SELECTOR, "h3").text.lower()
        assert "epic sadface" in error
        screenshot(driver, "login_vacio")
    finally:
        driver.quit()
