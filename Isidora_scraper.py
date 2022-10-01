from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import get_context, Process, Pool
from time import perf_counter
import csv
import time
from logging import root
import pandas
import requests
import re
from requests import Session
from bs4 import BeautifulSoup

# options.headless = True


# driver.implicitly_wait(10)
root_url = "https://www.immoweb.be/en"
search_apartment_url = root_url + "/search/apartment/for-sale" 
search_house_url = root_url + "/search/house/for-sale" 
#driver.get(search_apartment_url + "?page=1")



# def get_max_pages():
# # # Filter the empty items from the list and then change the list as a "set" so the duplicate are automatically removed

#     page_list = [elem.text for elem in driver.find_elements(By.XPATH, "//*[contains(text(), 'Page')]")]
# # # Get all elements of the page that has the word "Page" and put it in a list
#     page_list = set((list(filter(None, page_list))))
#     page_regex = re.compile("Page+\s")
#     max = 0
#     for string in page_list:
#         string = page_regex.sub('', string)
#         if max < int(string):
#             max = int(string)
#     return max



def search_property_urls(i):
    start_time = perf_counter()

    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    
    #print(f"PAGE N°{i}")
    driver.get(search_apartment_url + f"?page={i}")
    elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
    items = []
    for item in elements:
        # print(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))
        items.append(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))
    print(f"\nTime spent inside the loop: {perf_counter() - start_time} seconds.")
    driver.close()
    return items

with get_context("fork").Pool() as pool:
    gen = list(tuple(pool.map(search_property_urls, range(1, 334))))

with open("realestate_urls.csv", "w", newline='') as realestate_file:
    url_writer = csv.writer(realestate_file)

    url_writer.writerows(gen)
    #print(gen)

print("File saved")

# >>> with open('eggs.csv', newline='') as csvfile:
# ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# ...     for row in spamreader:
# ...         print(', '.join(row))

#print(gen)




