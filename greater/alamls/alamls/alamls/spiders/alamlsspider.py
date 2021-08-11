# -*- coding: utf-8 -*-
import scrapy
import re
import time
import csv

class AlamlsspiderSpider(scrapy.Spider):
    name = 'alamlsspider'
    
    def start_requests(self):
        
        default_url = "http://www.alamls.com/index.php?src=directory&view=Office&submenu=Office&srctype=Office_lister&pos={},15,456"
        
        for i in range(0, 32):
            value = i * 15
            
            url = default_url.format(value)
            print("URL---------------->", url)
            yield scrapy.Request(url=url, callback=self.first_page)
            return
            
    def first_page(self, response):
        time.sleep(2)
        
        # names = response.xpath("//table[@class='retsList']")
        names = response.xpath("//*[@id='interiorContent']/div[1]/main/div/table/tbody")
        
        
        
        print("names------------------------->", names)
