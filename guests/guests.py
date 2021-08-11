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

def page_source(htmlstring, driver):
    print("----------start--------------")
    
    # search_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    search_keys = ['a']

    for key in search_keys:
        name_input = driver.find_element_by_id("txtFirmName")
        name_input.send_keys(key)
        time.sleep(1)

        submitBtn = driver.find_element_by_id('btnSubmit')
        submitBtn.click()
        time.sleep(5)
        
        name_input = driver.find_element_by_id("txtFirmName")
        name_input.send_keys(Keys.CONTROL, 'a')
        name_input.send_keys(Keys.BACKSPACE)

        







if __name__ == "__main__":
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    driver.get("http://guests.themls.com/FindOffice.aspx")
    time.sleep(2)

    driver.maximize_window()

    page_source(driver.page_source, driver)