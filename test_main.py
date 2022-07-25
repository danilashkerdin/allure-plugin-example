import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Tests:

    @allure.id("101175")
    def test_google(self):
        driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get("https://www.google.com")
        time.sleep(3)

    @allure.id("101177")
    def test_yandex(self):
        driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get("https://www.yandex.ru")
        time.sleep(3)

    @allure.id("101176")
    def test_duck(self):
        """
        docstring

        try to delete @allure.id and assign test

        try with another test

        try to delete docstring and start launch then upload and try assign id once again

        """
        driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get("https://www.duckduckgo.com")
        time.sleep(3)
