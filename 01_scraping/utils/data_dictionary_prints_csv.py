from collections import defaultdict
import os
import pathlib
import pandas as pd
from utils.collect_property_data import Property
from requests import Session
from bs4 import BeautifulSoup
import json
from multiprocessing import pool
class PropertyDataWriter:
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

    def map_property_to_data_dictionary(file_name:str):
        i = 0
        property_data_dictionary = defaultdict(list)
        file_location = os.path.join(pathlib.Path(__file__).parent.resolve(), "../data", file_name)
        properties_url = pd.read_csv(file_location, encoding="utf-8")
        sess = Session()
        print(len(properties_url))
        print(type(properties_url))
        for property_url in properties_url.values:
            i += 1
            print(i)
            try :
                req = sess.get(property_url[0], timeout=2)
            except Exception as e:
                print("Some connection error")
                continue
            if req.status_code == 200:
                soup = BeautifulSoup(req.content, "html.parser")
                script = soup.find('script',attrs={"type" :"text/javascript"})
                print(property_url[0])
                property = Property(json.loads(script.contents[0][33:-10]))
                property_data_dictionary["id"].append(property.id)
                property_data_dictionary["locality"].append(property.locality)
                property_data_dictionary["postal_code"].append(property.postal_code)
                property_data_dictionary["region"].append(property.region)
                property_data_dictionary["province"].append(property.province)
                property_data_dictionary["type_of_property"].append(property.type)
                property_data_dictionary["subtype_of_property"].append(property.sub_type)
                property_data_dictionary["type_of_sale"].append(property.sale_type)
                property_data_dictionary["price"].append(property.price)
                property_data_dictionary["number_of_bedrooms"].append(property.bedroom_count)
                property_data_dictionary["surface"].append(property.surface)
                property_data_dictionary["kitchen_type"].append(property.kitchen_type)
                property_data_dictionary["fully_equipped_kitchen"].append(property.is_kitchen_fully_equipped)
                property_data_dictionary["furnished"].append(property.is_furnished)
                property_data_dictionary["open_fire"].append(property.has_open_fire)
                property_data_dictionary["terrace"].append(property.has_terrace)
                property_data_dictionary["terrace_surface"].append(property.terrace_surface)
                property_data_dictionary["garden"].append(property.has_garden)
                property_data_dictionary["garden_surface"].append(property.garden_surface)
                property_data_dictionary["number_of_facades"].append(property.facade_count)
                property_data_dictionary["land_surface"].append(property.land_surface)
                property_data_dictionary["swimming_pool"].append(property.has_swimming_pool)
                property_data_dictionary["state_of_the_building"].append(property.building_state)
        return property_data_dictionary

    def write_data_to_file():
        with open("urls.csv", "r") as f:
            data_file = pd.DataFrame(PropertyDataWriter.map_property_to_data_dictionary(f),columns=PropertyDataWriter.columns)
        data_file.to_csv("Property_structured_data3.csv")