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
import urllib.request
import random
import json


def parse_page(htmlstring, driver):
    phone = ""
    email = ""
    website = ""
    
    names = driver.find_elements_by_xpath("//table[@class='retsList']/tbody//tr/td[1]")
    
    print(len(names))
    
    for i in range(1, len(names) + 1):
        name = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[1]/a".format(i + 1)).text
        
        try:       
            street = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[2]/div[1]".format(i + 1)).text
        except:
            street = ""
        
        try:
            address = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[2]/div[2]".format(i + 1)).text
        except:
            address = ""    
        
        try:    
            phone = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[3]/div[1]/span[@class='phone']".format(i + 1)).text
        except:
            phone = ""
        
        try:
            email = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[3]/div[2]/a".format(i + 1)).text
        except:
            email = ""
            
        try:
            website = driver.find_element_by_xpath("//table[@class='retsList']/tbody//tr[{}]/td[3]/div[3]/a".format(i + 1)).text
        except:
            website = ""
    
        print("----------------------New Info----------------------")
        print("name-----------------> :", name)
        print("street---------------> :", street)
        print("address--------------> :", address)
        print("Phone----------------> :", phone)
        print("Email----------------> :", email)
        print("Website--------------> :", website)
        
        with open("alamls.csv", "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, street, address, phone, email, website])
    

if __name__ == "__main__":
    open('alamls.csv', 'wb').close()
    header = ["Name", "Street", "Address", "Phone", "Email", "Website"]
    with open('alamls.csv', "a", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
        
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    
    driver.maximize_window()
    time.sleep(2)
    
    default_url = "http://www.alamls.com/index.php?src=directory&view=Office&submenu=Office&srctype=Office_lister&pos={},15,456"
    
    for i in range(0, 32):  #32
        value = i * 15
        url = default_url.format(value)
        
        driver.get(url)
        parse_page(driver.page_source, driver)
        
        