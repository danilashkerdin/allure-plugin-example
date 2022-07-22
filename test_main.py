import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def test_google():
    driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://www.google.com")
    time.sleep(3)


def test_yandex():
    driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://www.yandex.ru")
    time.sleep(3)


def test_duck():
    driver = WebDriver(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://www.duckduckgo.com")
    time.sleep(3)
