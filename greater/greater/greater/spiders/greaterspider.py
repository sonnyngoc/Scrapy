# -*- coding: utf-8 -*-
import scrapy
import re
import csv


class GreaterspiderSpider(scrapy.Spider):
    name = 'greaterspider'
    output = 'greateralabamamls.csv'
    open(output, 'w').close()
    header = ['Name', 'Street', 'Locality', 'Region', 'Postal_Code', 'Phone', 'Fax', 'Email']
    with open(output, "a", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
        
    def start_requests(self):
        print("-------------start-------------")
        
        first_url = "https://www.greateralabamamls.com/AgentSearch/Results.aspx?SearchType=office&FirstName=&LastName=&OfficeName=&Address=&City=&State=&Country=-32768&Zip=&Languages=&Titles=&Specialties=&Accreditations=&Areas=&rpp=10&SortOrder="
        
        default_url = "https://www.greateralabamamls.com/AgentSearch/Results.aspx?SearchType=office&FirstName=&LastName=&OfficeName=&Address=&City=&State=&Country=-32768&Zip=&Languages=&Titles=&Specialties=&Accreditations=&Areas=&rpp=10&page={}&SortOrder="

        for i in range(1, 100):
            if i == 1:
                url = first_url
            else:
                url = default_url.format(i)
            yield scrapy.Request(url=url, callback=self.first_page)
            # return
    
    def first_page(self, response):
        item_urls = response.xpath("//div[@class='ao-info-c1']/h3/a/@href").extract()
        
        for item_url in item_urls:
            up_url = "https://www.greateralabamamls.com"
            url = up_url + item_url
            print(url)
            
            yield scrapy.Request(url, callback=self.item_parse)
            # return
            
    def item_parse(self, response):
        name = ""
        street = ""
        locality = ""
        region = ""
        postal_code = ""
        phone = ""
        fax = ""
        email = ""
        
        name = response.xpath("//h2[@itemprop='name']/text()").get()
        name = ''.join(name).strip() if name else ""
        
        street = response.xpath("//span[@itemprop='street-address']/text()").get()
        street = ''.join(street).strip() if street else ""
        
        locality = response.xpath("//span[@itemprop='locality']/text()").get()
        
        region = response.xpath("//span[@itemprop='region']/text()").get()
        
        postal_code = response.xpath("//span[@itemprop='postal-code']/text()").get()
        
        phone = response.xpath("//span[@id='office-phone-main']/text()").get()
        
        fax = response.xpath("//span[@id='office-phone-fax']/text()").get()
        
        # email = response.xpath("//div[@id='office-email']/a[@class='rui-icon-link-text']/text()")
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
        email = emails[1]
        

        print("-------------------------------------------")
        print("Name-------------->, : ", name)
        print("street------------>, : ", street)
        print("locality---------->, : ", locality)
        print("region------------>, : ", region)
        print("postal_code------->, : ", postal_code)
        print("phone------------->, : ", phone)
        print("fax--------------->, : ", fax)
        print("email------------->, : ", email)
        
        with open(self.output, "a", newline="", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, street, locality, region, postal_code, phone, fax, email])
        
            
            
            

            