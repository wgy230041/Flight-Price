# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:43:22 2018
缓存存在网页，抓取不需要reload
notepade
Entering \s+ on the Find what field and \n (Change to \n\n for two new lines) on the Replace With field followed by Replace All transforms:

store datas in list
@author: wgy
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import selenium
import requests
import json
from lxml import etree
import csv
import re


#airport = ["JFK", "PVG","","","",""]

#for ap in airport:
#Input1 = input("Please enter your depart location (or keywords like JFK): ")
#Input2 = input("Please enter your destination (or keywords like JFK): ")
#print("Thank you, you entered: ",Inputs1， " to ", Input2 )
#APIKey =  "AIzaSyCRPqoodoC09gCFvfUP_kzwS9qIi8XI1KE"
#page = requests.get("https://www.google.fr/flights#" + Input1 + Input2+ ".2018-12-25;c:USD;e:1;so:1;sd:1;t:f;tt:o")
        
driver =  webdriver.Firefox(executable_path='D:/ECSU CSC-360  Advanced Web Development and Web Scraping/Assingment/final projects/geckodriver.exe')
driver.get("https://www.google.fr/flights#flt=JFK.PVG.2018-12-25;c:USD;e:1;so:1;sd:1;t:f;tt:o")
#time.sleep(1)  
#"gws-flights-results__dominated-toggle flt-subhead2 gws-flights-results__collapsed").click()
# jstcache = 9367

for i in range(100000) :   
    try :
        elem = driver.find_element_by_class_name("gws-flights-results__dominated-link")
        break
    except :       
        print("not found, trying again")
        if i == 9999 :
            assert False, "timeout getting gws-flights-results__dominated-link"        

elem.click()


time.sleep(5)
#driver.save_screenshot(r'flight_explorer.png') 
  
#lists = driver.find_element_by_xpath("//li[@class='gws-flights-results__collapsed-itinerary gws-flights-results__itinerary']//*[text()='Testing']")
#driver.find_element_by_class_name("gws-flights-results__has-dominated gws-flights-results__result-list")
#driver.find_element_by_class_name("gws-flights-results__expanded-itinerary .gws-flights-results__itinerary")

#lists = driver.find_elements_by_tag_name("li")
#lists = driver.find_elements_by_xpath("//li")
#lists = driver.find_elements_by_xpath("//li/@class")  *raise exception_class(message, screen, stacktrace)
#lists = driver.find_elements_by_xpath("//li[@class='gws-flights-results__collapsed-itinerary gws-flights-results__itinerary']")


#assert False, "stopping here"

times =[]
airlineNo =[]
fPrices =[]
FPrices=[]
arrivals=[]
departs=[]
flightsNos=[]
fstops=[]
fdurations=[]
#get rows by the div class
#d = driver.find_elements_by_class_name("gws-flights-results__collapsed-itinerary")
prices = driver.find_elements_by_class_name("gws-flights-results__itinerary-price")
#len(prices)
for p in prices:    
    fPrices.append(p.text)
    #while '' in fPrices:
    FPrices=[x for x in fPrices if x]
    #FPrices=fPrices.remove('')
#filtered = re.match(r'^\s*$', '', fPrices) #TypeError: unhashable type: 'list'
# line is empty (has only the following: \t\n\r and whitespace)
#https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
#len(FPrices)
#print(FPrices)

durations = driver.find_elements_by_class_name("gws-flights-results__duration")
for d in durations :   
#    print(d.text) 
    fdurations.append(d.text)
#len(durations)
stops = driver.find_elements_by_class_name("gws-flights-results__stops")
for s in stops : 
#   print(s.text)
    fstops.append(s.text)

time.sleep(0.01)    
times = driver.find_elements_by_class_name("gws-flights-results__times")
#arrivals = times.text.find_elements_by_tag_name("span")
for t in times:
    depart = t.text.split(" ")[0]+ t.text.split(" ")[1]
    departs.append(depart)
    arrival = t.text.split(" ")[3] + t.text.split(" ")[4]
    arrivals.append(arrival)

#print(arrivals)
#print(departs)

#departs = arrivals[0].find_elements_by_tag_name("span")
#print(duration.text)


with open('price.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    for m in range(len(FPrices)):
        writer.writerow(['', '', '', departs[m], arrivals[m], fdurations[m], fstops[m], FPrices[m]]) 

csvfile.close() 


#assert False, "stopping here"


#price = driver.find_element_by_class_name("gws-flights-results__itinerary-price").text
#price = driver.find_element_by_class_name("flt-subhead1.gws-flights-results__price.gws-flights-results__cheapest-price").text
#price = driver.find_elements_by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[1]//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]/div[@class='gws-flights-results__collapsed-itinerary gws-flights-results__itinerary']/div[@class='gws-flights-results__itinerary-price']//jsl[.='$674']")
#price = driver.find_elements_by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[8]//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]/div[@class='gws-flights-results__collapsed-itinerary gws-flights-results__itinerary']/div[@class='gws-flights-results__itinerary-price']//jsl[.='$964']")
#price = driver.find_elements_by_xpath("//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]/div[@class='gws-flights-results__collapsed-itinerary gws-flights-results__itinerary']/div[@class='gws-flights-results__itinerary-price']")
#print(price.text)
#stops = driver.find_element_by_class_name("gws-flights-results__stops flt-subhead1Normal gws-flights-results__has-warning-icon")
    

#stops = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[3]/div/div[2]/main[2]/div[9]/div[1]/div[3]/div[5]/div[5]/div[1]/ol/li[1]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div/div[1]/span[1]/jsl[3]")
#stops = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[3]/div/div[2]/main[2]/div[9]/div[1]/div[3]/div[5]/div[5]/div[1]/ol/li[2]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div/div[1]/span[1]/jsl[2]")
#stops = driver.find_element_by_xpath("//html/body/div[2]/div[2]/div[3]/div/div[2]/main[2]/div[9]/div[1]/div[3]/div[5]/div[5]/div[1]/ol/li[19]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div/div[1]/span[1]/jsl[1]")
#stops = driver.find_element_by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[8]/div/div[1]/div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]//jsl[.='Nonstop']")
#stops = driver.find_element_by_xpath("//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[2]/div[@class='gws-flights-results__more']").click()
#print(stops.text)
    
#duration = driver.find_element__by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[1]//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]//div[.='34h 5m']")
#duration = driver.find_element__by_xpath("//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]//div[.='34h 5m']")
#duration = driver.find_element_by_class_name("gws-flights-results__duration flt-subhead1Normal")
#print(duration.text)
#time.sleep(0.01)
#duration = driver.find_element_by_class_name("gws-flights-results__duration flt-subhead1Normal")
#print(duration.text)    
    
#departs = driver.find_elements_by_xpath(//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[1]//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]//div[.='34h 5m']")
#departs = driver.find_elements_by_xpath("//f//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[1]")
    
#Times = driver.find_elements_by_tag_name("jsl").text
#times.append(Times)
#print(departs.text)
#time.sleep(0.01) 
#depart = driver.find_elements_by_tag_name("aria-label").text
#arrival = driver.find_elements_by_tag_name("aria-label")
#times.append(arrival.text)
#print(times)
time.sleep(1)   
#element is not clickable at point in selenium webdriver chrome python
#http://learn-automation.com/how-to-solve-element-is-not-clickable-at-pointxy-in-selenium/    
#How to solve Element is not clickable at point in Selenium
#details = driver.find_elements_by_class_name("gws-flights-results__expand").click()

details = driver.find_elements_by_class_name("gws-flights-results__more")
#details = driver.find_elements_by_class_name("gws-flights-results__expand").click()
#details = driver.find_elements_by_xpath("//div[@class='gws-flights-results__expand']").click()
#details = driver.find_elements_by_xpath("//div[@role='button']")
#details = driver.find_elements_by_xpath("//div[@class='gws-flights-results__more']").click()
#details = driver.find_elements_by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]//div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[1]//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[2]/div[@class='gws-flights-results__more']").click()
#details = driver.find_elements_by_xpath("//f//div[@class='gws-flights-results__itinerary-card-summary gws-flights-results__result-item-summary gws-flights__flex-box']/div[2]/div[@class='gws-flights-results__more']").click()
#details = driver.find_elements_by_xpath("//div[@class='gws-flights-results__expand']")
for position in details:
    for j in range(1000000000) :   
        try :
            driver.execute_script("arguments[0].click();", position)
            time.sleep(2) # when reach the clicked one will stop
            break
        except :       
            print("not found, trying again")
            if i == 999999999 :
                assert False, "timeout getting gws-flights-results__expand details"   
                
                
#assert False, "stop here"

time.sleep(10) 
# try to split into even and odd lists and store the even list
Numbers = driver.find_elements_by_class_name("gws-flights-results__other-leg-info")
#Number = driver.find_elements_by_xpath("//div[@id='flt-app']/div[@class='gws-flights__flex-column gws-flights__flex-grow']/main[2]/div[9]/div[@class='gws-flights-results__results-container gws-flights__center-content']/div[3]/div[5]//div[@role='region']/ol[@class='gws-flights-results__has-dominated gws-flights-results__result-list']/li[52]/div/div[@class='gws-flights-widgets-expandablecard__body']/div[2]//span[.='5976']")
#Number = driver.find_elements_by_xpath("//f/div/div[@class='gws-flights-widgets-expandablecard__body']/div[2]")
# len(Numbers)
#for i in range(len(Numbers)):
#    if i %2 !=0:
#        Fnumbers.append(Numbers[i].text)
#        print(fNumbers)
for n in Numbers:
    flightNo = n.text
    #print(flightNo)
for i in range(len(flightNo)): 
    if i %2 !=0:
        for f in flightNo:
            fligtsnumber= f.split("\n")[-1]
            flightsNos.append(fligtsnumber) 
            print(flightsNos)
      
#the flight is same flight number case like the A has 1 stop with some layout time, then take same flight number.   
#print(flights)
#time.sleep(1) 

with open('price.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    for m in range(len(FPrices)):
        writer.writerow(['', '', '', departs[m], arrivals[m], fdurations[m], fstops[m], FPrices[m]]) 

csvfile.close() 
#driver.get('http://www.python.org/')
#driver.save_screenshot('screenshot.png')
#driver.quit()
       
