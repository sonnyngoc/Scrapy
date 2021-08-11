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
import json, re


def parse_page(htmlstring, driver):
    print("--------------------START---------------------")
    detail_Btns = driver.find_elements_by_xpath("//table[@class='rgMasterTable']/tbody//tr/td[1]")
    
    for page in range(1, 238):
        if page >= 200:
            for i in range(1, len(detail_Btns) + 1):
                
                phone_data = {
                    "phone1" : "",
                    "phone2" : "",
                    "phone3" : "",
                    "phone34" : ""
                }

                email_data = {
                    "email1" : "",
                    "email2" : "",
                    "email3" : "",
                    "email4" : ""
                }
                
                last_name = driver.find_element_by_xpath("//table[@class='rgMasterTable']/tbody/tr[{}]/td[2]".format(i)).text 
                
                first_name = driver.find_element_by_xpath("//table[@class='rgMasterTable']/tbody/tr[{}]/td[3]".format(i)).text
                
                company_name = driver.find_element_by_xpath("//table[@class='rgMasterTable']/tbody/tr[{}]/td[4]".format(i)).text
                
                city = driver.find_element_by_xpath("//table[@class='rgMasterTable']/tbody/tr[{}]/td[5]".format(i)).text
                
                detail_btn = driver.find_element_by_xpath("//table[@class='rgMasterTable']/tbody//tr[{}]/td[1]/a".format(i))
                
                driver.execute_script("arguments[0].click();", detail_btn)
                time.sleep(2)
                
                phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', driver.page_source)

                emails = re.findall(r'[\w\.-]+@[\w\.-]+', driver.page_source)
                
                for phone in range(1, len(phones) + 1):
                    phone_data["phone{}".format(phone)] = phones[phone - 1]
                        
                for email in range(1, len(emails) + 1):
                    if email % 2 == 1:
                        email_data["email{}".format(email)] = emails[email - 1]

                
                print("Last Name----------------------> : ", last_name)
                print("First Name---------------------> : ", first_name)
                print("Company Name-------------------> : ", company_name)
                print("City---------------------------> : ", city)
                print("Phone--------------------------> : ", phone_data)
                print("Email--------------------------> : ", email_data)
                
                with open("columbus22.csv", "a", newline="", encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([last_name, first_name, company_name, city, phone_data["phone1"], phone_data["phone2"], email_data["email1"], email_data["email3"]])
                
                back_btn = driver.find_element_by_id("ctl00_body_primary_body_1_ctl01_ucSearchResults_lkbBackToSearch")
                
                driver.execute_script("arguments[0].click();", back_btn)
                time.sleep(0.3)
            
        nextpage_Btn = driver.find_element_by_class_name("rgPageNext")
        driver.execute_script("arguments[0].click();", nextpage_Btn)  
        time.sleep(0.3)      
        

if __name__ == "__main__":
    
    open('columbus22.csv', 'wb').close()
    header = ["Last Name", "First Name", "Company Name", "City", "Phone1", "Phone2", "Email1", "Email2"]
    with open('columbus22.csv', "a", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
    
    path = "driver\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    
    driver.maximize_window()
    time.sleep(2)
    
    driver.get("https://columbusrealtors.com/find.aspx?mode=browse&letter=")
    parse_page(driver.page_source, driver)
    
    
    