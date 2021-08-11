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
    print("-------------------START------------------")

    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(iframes[2])
    
    searchBtn = driver.find_element_by_id("m_btnSearch")
    searchBtn.click()
    time.sleep(2)
    
    first_item = driver.find_elements_by_class_name("d127m5")
    first_item[0].click()
    time.sleep(2)
    
    for x in range(1, 25):
        if x <= 10 :
            counts = 12
        else:
            counts = 7
        for i in range(1, counts):
            if i != 1:
                nextBtn = driver.find_element_by_xpath("//ul[@class='pagination mtx-pagination']/li[{}]/a".format(i))
                nextBtn.click()
                time.sleep(1)

            name = driver.find_element_by_xpath("//td[@class='d130m10']//span[@class='field']").text
            address = driver.find_element_by_xpath("//td[@class='d130m10']//span[@class='wrapped-field']").text
            city_state_zip = driver.find_element_by_xpath('//*[@id="wrapperTable"]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/span').text
            
            office_contact = driver.find_element_by_xpath("//td[@class='d130m15']//span[@class='wrapped-field']").text
            phone_fax = driver.find_elements_by_xpath("//td[@class='d130m8']//span[@class='field']")
            phone = phone_fax[0].text
            fax = phone_fax[1].text
            
            email_web = driver.find_elements_by_xpath("//td[@class='d130m15']//span[contains(@class, 'formula') and contains(@class, 'field')]")
            
            email = email_web[0].text
            web = email_web[1].text
                
            print("Name----------------> : ", name)
            print("Address-------------> : ", address)
            print("City_state_zip------> : ", city_state_zip)
            print("Office Contact------> : ", office_contact)
            print("Phone---------------> : ", phone)
            print("Fax-----------------> : ", fax)
            print("Email---------------> : ", email)
            print("Web-----------------> : ", web)
            print("-----------------------------------------------------")
            with open("tuscal.csv", "a", newline="", encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([name, address, city_state_zip, office_contact, phone, fax, email, web])
        if x == 1:
            nextPage = driver.find_element_by_xpath("//ul[@class='pagination mtx-pagination']/li[{}]/a".format(11))
        elif x <= 10:
            nextPage = driver.find_element_by_xpath("//ul[@class='pagination mtx-pagination']/li[{}]/a".format(12))
        else:
            nextPage = driver.find_element_by_xpath("//ul[@class='pagination mtx-pagination']/li[{}]/a".format(7))
        nextPage.click()
        time.sleep(1)

if __name__ == "__main__":
    
    open('tuscal.csv', 'wb').close()
    header = ["Name", "Address", "City/State/Zip", "office_contract", "Phone", "Fax", "Email", "Website"]
    with open('tuscal.csv', "a", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
    
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    
    driver.maximize_window()
    time.sleep(2)
    
    driver.get("https://www.tuscaloosamls.com/find-an-office")
    parse_page(driver.page_source, driver)