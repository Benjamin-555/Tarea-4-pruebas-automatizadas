import time
from selenium.webdriver.common.by import By
from driver_factory import get_driver, screenshot

URL = "https://www.saucedemo.com/"


def login(driver):
    driver.get(URL)
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


def test_add_to_cart():
    driver = get_driver()
    try:
        login(driver)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1"

        screenshot(driver, "agregar_carrito")
    finally:
        driver.quit()


def test_remove_from_cart():
    driver = get_driver()
    try:
        login(driver)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)

        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0

        screenshot(driver, "remover_carrito")
    finally:
        driver.quit()


def test_checkout():
    driver = get_driver()
    try:
        login(driver)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)

        driver.find_element(By.ID, "first-name").send_keys("Juan")
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "postal-code").send_keys("10101")

        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

        msg = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert msg == "THANK YOU FOR YOUR ORDER"

        screenshot(driver, "checkout_completado")

    finally:
        driver.quit()
