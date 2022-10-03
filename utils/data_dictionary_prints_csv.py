from collections import defaultdict
import collections
import os
import pathlib
import pandas as pd
from utils.collect_property_data import Property

class PropertyDataWriter:
    columns = [
        "locality",
        "type_of_property",
        "subtype_of_property",
        "type_of_sale",
        "price",
        "number_of_bedrooms",
        "surface",
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
        property_data_dictionary = defaultdict(list)
        file_location = os.path.join(pathlib.Path(__file__).parent.resolve(), "../data", file_name)

        with open(file_location, "r", encoding="utf-8") as file:
            for i in range(6):
                property_url = file.readline()
                print(property_url)
                property = Property(property_url)

                property_data_dictionary["locality"].append(property.locality)
                property_data_dictionary["type_of_property"].append(property.type)
                property_data_dictionary["subtype_of_property"].append(property.sub_type)
                property_data_dictionary["type_of_sale"].append(property.sale_type)
                property_data_dictionary["price"].append(property.price)
                property_data_dictionary["number_of_bedrooms"].append(property.bedroom_count)
                property_data_dictionary["surface"].append(property.surface)
                property_data_dictionary["fully_equipped_kitchen"].append(property.is_kitchen_fully_equipped)
                property_data_dictionary["furnished"].append(property.is_furnished)
                property_data_dictionary["open_fire"].append(property.has_open_fire)
                property_data_dictionary["terrace"].append(property.has_terrace)
                property_data_dictionary["terrace_surface"].append(property.terrace_surface)
                property_data_dictionary["garden"].append(property.has_garden)
                property_data_dictionary["garden_surface"].append(property.garden_surface)
                property_data_dictionary["land_surface"].append(property.land_surface)
                property_data_dictionary["number_of_facades"].append(property.facade_count)
                property_data_dictionary["swimming_pool"].append(property.has_swimming_pool)
                property_data_dictionary["state_of_the_building"].append(property.building_state)
        
        return property_data_dictionary

    def write_data_to_file():
        data_file = pd.DataFrame(PropertyDataWriter.map_property_to_data_dictionary("realestate_urls.csv"),columns=PropertyDataWriter.columns)
        data_file.to_csv("Property_structured_data.csv")
