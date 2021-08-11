# -*- coding: utf-8 -*-
import scrapy
import csv

class RecolspiderSpider(scrapy.Spider):
    name = 'recolspider'
    
    output = "recolorado.csv"
    open(output, 'w').close()
    header = ['Agent Name', 'Agent Title', 'Agent Street', 'Agent City', 'Agent State', 'Agent Zip', 'Agent Cell', 'Agent Office']

    with open(output, "a", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        csv_writer.writeheader()
    
    def start_requests(self):
        print("------------------Scrapy Start---------------")
        for i in range (1, 576):  #576
            first_url = "https://www.recolorado.com/offices/{}-pg/".format(i)
            print(first_url)

            yield scrapy.Request(url=first_url, callback=self.parse_page)
    
    def parse_page(self, response):
        item_urls = response.xpath("//a[contains(@class, 'button__agents')]/@href").extract()

        for item_url in item_urls:
            second_url = "https://www.recolorado.com" + item_url

            yield scrapy.Request(url=second_url, callback=self.item_parse)
            # return
    def item_parse(self, response):

        agent_name = ""
        agent_title = ""
        agent_street = ""
        agent_city = ""
        agent_state = ""
        agent_zip = ""
        agent_cell = ""
        agent_office = ""
        
        agent_titles = response.xpath("//h5[@class='results--agent-title']/text()").extract()

        count = 1
        for agent_title in agent_titles:
            print(agent_title)
            if "Managing" in agent_title:
                agent_name = response.xpath("(//h4[contains(@class, 'results--name-text__agent')])[{}]/text()".format(count)).get()
                agent_title = "Managing Broker"
                agent_street = response.xpath("(//span[@class='results--address-street'])[{}]/text()".format(count)).get().replace(",", "")
                agent_city = response.xpath("(//span[@class='results--address-city '])[{}]/text()".format(count)).get().replace(", ", "")
                agent_state = response.xpath("(//span[@class='results--address-state '])[{}]/text()".format(count)).get()
                agent_zip = response.xpath("(//span[@class='results--address-zip '])[{}]/text()".format(count)).get()
                try:
                    agent_cell = response.xpath("(//a[contains(@class, 'results--phonenumber__agentcell')])[{}]/text()".format(count)).get().replace("Cell: ", "")
                except:
                    agent_cell = ""
                try:
                    agent_office = response.xpath("(//a[contains(@class, 'results--phonenumber__agentoffice')])[{}]/text()".format(count)).get().replace("Office: ", "")
                except:
                    agent_office = ""
                print("-----------------------------------------------------")
                print("Agent Name-------------------> : ", agent_name)
                print("Agent Title------------------> : ", agent_title)
                print("Agent Street-----------------> : ", agent_street)
                print("Agent City-------------------> : ", agent_city)
                print("Agent State------------------> : ", agent_state)
                print("Agent Zip--------------------> : ", agent_zip)
                print("Agent Cell-------------------> : ", agent_cell)
                print("Agent Office-----------------> : ", agent_office)
                with open(self.output, "a", newline="", encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([agent_name, agent_title, agent_street, agent_city, agent_state, agent_zip, agent_cell, agent_office])
            count += 1


        


