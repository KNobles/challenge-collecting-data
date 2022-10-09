from collections import defaultdict
from email.policy import default
import json
from multiprocessing import get_context
import os
import pathlib
from threading import Thread
from utils.url_scraper import Scraper
from utils.collect_property_data import Property
from utils.data_dictionary_prints_csv import PropertyDataWriter
import requests
from requests import Session
import re
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing.pool import ThreadPool

print("========================================================")
print("\tWELCOME TO THE COLLECTING DATA CHALLENGE")
print("========================================================\n")

# while True:
#     answer = input("Would you like to create a new set of data? [Y/n] ").lower()
#     if answer == "y":
#         Scraper.write_property_urls()
#         break
#     elif answer == "n":
#         break
#     else:
#         print("Answer needs to be [Y] or [n]\n")
columns = [
    "id",
    "locality",
    "postal_code",
    "region",
    "province",
    "type_of_property",
    "subtype_of_property",
    "type_of_sale",
    "price",
    "number_of_bedrooms",
    "surface",
    "kitchen_type",
    "fully_equipped_kitchen",
    "furnished",
    "open_fire",
    "terrace",
    "terrace_surface",
    "garden",
    "garden_surface",
    "land_surface",
    "number_of_facades",
    "swimming_pool",
    "state_of_the_building"
]

# PropertyDataWriter.write_data_to_file()
dic = defaultdict(list)
thread_list = list()
i = 0
with open("01_scraping/data/urls.csv", "r") as f:
    for url in f.readlines():
        th = Thread(target=PropertyDataWriter.append_to_dict, args=[url, dic])
        th.start()
        thread_list.append(th)
    
    for thread in thread_list:
        print(i)
        thread.join()
        i += 1
        
write = pd.DataFrame(data=dic, columns=columns)
write.to_csv("big_data.csv", index=False)
