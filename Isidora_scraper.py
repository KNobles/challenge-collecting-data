from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread
from time import perf_counter
import time
from logging import root
import pandas
import requests
import re
from requests import Session
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.headless = True
driver.implicitly_wait(10)
root_url = "https://www.immoweb.be/en"
search_apartment_url = root_url + "/search/apartment/for-sale" 
search_house_url = root_url + "/search/house/for-sale" 

driver.get(search_apartment_url + "?page=1")

# # Get all elements of the page that has the word "Page" and put it in a list
page_list = [elem.text for elem in driver.find_elements(By.XPATH, "//*[contains(text(), 'Page')]")]

# # Filter the empty items from the list and then change the list as a "set" so the duplicate are automatically removed
page_list = set((list(filter(None, page_list))))

def get_max_pages():
    page_regex = re.compile("Page+\s")
    max = 0
    for string in page_list:
        string = page_regex.sub('', string)
        if max < int(string):
            max = int(string)
    return max
# def scrap_page_urls()
# elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
# print(len(elements))

#for apartments
def search_property_urls(search_url):
    driver.get(root_url)
    driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()
    for i in range (1, get_max_pages()):
        print(f"PAGE N°{i}")
        driver.get(search_url + f"?page={i}")
        elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')

        for item in elements:
            print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))   
    return        

search_property_urls(search_apartment_url)
#0.8927087783813477 seconds
# search_apartments(search_apartment_url, driver)

#multi threading
# threads = list()
# for i in range(5):
#     start_time = time.time()
#     print("=============================")
#     print(f"THREAD NUMBER = {i}")
#     print("=============================")
#     thread = Thread(target=search_apartments(search_apartment_url), args=(i,)) # New thread will run "task" with argument "i"
#     threads.append(thread) # To keep track of all the treads
#     print("--- %s seconds ---" % (time.time() - start_time))     

# for thread in threads:
#     thread.start()

# for thread in threads:  # The second loop is necessary. start() everything then join() everything.
#     thread.join() # Make sure all the threads are done before continuing

# print(f"\nTime spent inside the loop: {perf_counter() - start_time} seconds.")

