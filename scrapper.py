from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread
from time import perf_counter
import time
from logging import root
import pandas
import requests
from requests import Session
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(10)
root_url = "https://www.immoweb.be/en"
page_num = 1
search_apartment_url = root_url + "/search/apartment/for-sale" + "?page=" 
search_house_url = root_url + "/search/house/for-sale" + "?page=" 


driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]').click()

# def scrap_page_urls()
# elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
# print(len(elements))

#for apartments
def search_apartments(search_url):
    for i in range (1, 334):
        start_time = time.time()
        print(i)
        driver.get(search_url + str(i))
        elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
        print("--- %s seconds ---" % (time.time() - start_time))        

        for item in elements:
            print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))
    return        

#0.8927087783813477 seconds
# search_apartments(search_apartment_url, driver)

#multi threading
threads = list()
for i in range(5):
    thread = Thread(target=search_apartments(search_apartment_url, driver), args=(i,)) # New thread will run "task" with argument "i"
    threads.append(thread) # To keep track of all the treads

for thread in threads:
    thread.start()

for thread in threads:  # The second loop is necessary. start() everything then join() everything.
    thread.join() # Make sure all the threads are done before continuing

# print(f"\nTime spent inside the loop: {perf_counter() - start_time} seconds.")

