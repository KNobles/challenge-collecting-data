from logging import root
import pandas
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests import Session
from bs4 import BeautifulSoup

## "isLifeAnnuitySale": false ===>>> SHOULD BE FALSE

root_url = "https://www.immoweb.be/en"
search_house_url = root_url + "/search/house/for-sale"
search_appartment_url = root_url + "/search/apartment/for-sale"
page_regex = re.compile("Page+\s")

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(search_appartment_url)
driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()

# # Get all elements of the page that has the word "Page" and put it in a list
page_list = [elem.text for elem in driver.find_elements(By.XPATH, "//*[contains(text(), 'Page')]")]

# # Filter the empty items from the list and then change the list as a "set" so the duplicate are automatically removed
page_list = set((list(filter(None, page_list))))

def get_max_pages():
    max = 0
    for string in page_list:
        string = page_regex.sub('', string)
        if max < int(string):
            max = int(string)
    return max


for i in range(1, 10):
    driver.get(search_appartment_url + f"?isAPublicSale=true&page={i}")
    elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
    for item in elements:
        print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))

driver.close()