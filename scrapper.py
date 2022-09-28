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
search_house_url = root_url + "/search/house/for-sale"
search_appartment_url = root_url + "/search/apartment/for-sale"

driver.get(search_appartment_url)
driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()
elements = driver.find_elements(By.CLASS_NAME, "card__title-link")

for item in elements:
    if item.get_attribute("href") == "":
        print("its the end")
    else:
        print(item.get_attribute("href"))

#.get_attribute("href")
#driver.find_element(By.ID, "uc-btn-accept-banner").click()
# print(driver.find_element(By.TAG_NAME, "ul").get_attribute())