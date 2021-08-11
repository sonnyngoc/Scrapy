import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from lxml import html
import csv
import time
import random
import json
import re, math



def parse_page(htmlstring, driver):
    print("-----------------------START-----------------------")
    searchBtn = driver.find_element_by_xpath("//td[@id='search_basic']//button")
    searchBtn.click()


if __name__ == "__main__":
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    driver.get("http://mlssaz.com/agent_search.html")
    time.sleep(2)
    driver.maximize_window()

    parse_page(driver.page_source, driver)
