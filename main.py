import json
import os
import pathlib
from utils.url_scraper import Scraper
from utils.collect_property_data import Property
from utils.data_dictionary_prints_csv import PropertyDataWriter
import requests
from requests import Session
import re
from bs4 import BeautifulSoup

print("========================================================")
print("\tWELCOME TO THE COLLECTING DATA CHALLENGE")
print("========================================================\n")
# with Session() as sess:
#     for i in range(11):
#         req = sess.get("https://www.immoweb.be/en/classified/town-house/for-sale/bruxelles/1000/10065434?searchId=633bf84d83949")
#         soup = BeautifulSoup(req.content, "html.parser")
#         script = soup.find('script',attrs={"type" :"text/javascript"})
#         print(json.loads(script.contents[0][33:-10]))
#         print(req.headers)

# while True:
#     answer = input("Would you like to create a new set of data? [Y/n] ").lower()
#     if answer == "y":
#         Scraper.write_property_urls()
#         break
#     elif answer == "n":
#         break
#     else:
#         print("Answer needs to be [Y] or [n]\n")

# prop = Property("https://www.immoweb.be/en/classified/apartment/for-sale/antwerp/2020/10145899?searchId=63399cae2b8c2")
# print(prop.building_state)
# print(prop.property_sub_type)
# print(prop.property_building_state)

# prop = Property("https://www.immoweb.be/en/classified/town-house/for-sale/bruxelles/1000/10065434?searchId=633bf84d83949")
# print(prop.property_data()["property"]["hasTerrace"])
# print(prop.is_kitchen_fully_equipped)
# print(prop.property_type)
# print(prop.property_data)

PropertyDataWriter.write_data_to_file()
