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
import pandas as pd

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


PropertyDataWriter.write_data_to_file()