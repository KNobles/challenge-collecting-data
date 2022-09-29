from logging import root
import pandas
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests import Session
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(7)
root_url = "https://www.immoweb.be/en"
page_num = 1
search_house_url = root_url + "/search/house/for-sale" + "?page=" 
search_appartment_url = root_url + "/search/apartment/for-sale" + "?page=" 

driver.get(search_appartment_url)
driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()

# def scrap_page_urls()
# elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
# print(len(elements))

#for apartments
for j in range (1, 334):
    print(j)
    driver.get(search_appartment_url + str(j))
    elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')

    for item in elements:
        print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))
        
#for houses
for j in range (1, 334):
    print(j)
    driver.get(search_house_url + str(j))
    elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')

    for item in elements:
        print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))



# Get last page from pagination list



#.get_attribute("href")
#driver.find_element(By.ID, "uc-btn-accept-banner").click()
# print(driver.find_element(By.TAG_NAME, "ul").get_attribute())