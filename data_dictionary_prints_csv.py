import pandas as pd
from utils.collect_property_data import Property

columns = [
    "type_of_property",
    "subtype_of_property",
    "locality",
    "type_of_sale",
    "price",
    "number_of_rooms",
    "area",
    "fully_equipped_kitchen",
    "furnished",
    "open_fire",
    "terrace",
    "garden",
    "number_of_facades",
    "swimming_pool"
]

def map_property_to_data_dictionary(property_data_dictionary, property: Property):
    property_data_dictionary["type_of_property"] = property_data_dictionary.get("type_of_property",[]) + [property.property_type]
    property_data_dictionary["subtype_of_property"] = property_data_dictionary.get("subtype_of_property", []) + [property.property_sub_type]
    property_data_dictionary["locality"] = property_data_dictionary.get("locality",[]) + [property.property_locality]
    property_data_dictionary["type_of_sale"] = property_data_dictionary.get("type_of_sale", []) + [property.property_sale_type]
    property_data_dictionary["price"] = property_data_dictionary.get("price", []) + [property.property_price]
    property_data_dictionary["number_of_rooms"] = property_data_dictionary.get("number_of_rooms", []) + [property.property_room_count]
    property_data_dictionary["area"] = property_data_dictionary.get("area", []) + [property.property_surface]
    property_data_dictionary["fully_equipped_kitchen"] = property_data_dictionary.get("fully_equipped_kitchen", []) + [property.property_is_kitchen_fully_equipped]
    property_data_dictionary["furnished"] = property_data_dictionary.get("furnished", []) + [property.property_is_furnished]
    property_data_dictionary["open_fire"] = property_data_dictionary.get("open_fire", []) + [property.property_has_open_fire]
    property_data_dictionary["terrace"] = property_data_dictionary.get("terrace", []) + [property.property_has_terrace]
    property_data_dictionary["garden"] = property_data_dictionary.get("garden", []) + [property.property_has_garden]
    # property_data_dictionary["number_of_facades"] = property_data_dictionary.get("number_of_facades", []) + [property.property_facade_count]
    property_data_dictionary["swimming_pool"] = property_data_dictionary.get("swimming_pool", []) + [property.property_has_swimming_pool]
    # property_data_dictionary["terrace_area"] = property_data_dictionary.get("terrace_area", []) + [property.terrace_area]
    # property_data_dictionary["garden_area"] = property_data_dictionary.get("garden_area", []) + [property.garden_area]
    # property_data_dictionary["surface_of_the_land"] = property_data_dictionary.get("surface_of_the_land", []) + [property.surface_of_the_land]
    # property_data_dictionary["surface_of_the_plot"] = property_data_dictionary.get("surface_of_the_plot", []) + [property.surface_of_the_plot]
    # property_data_dictionary["state_of_the_building"] = property_data_dictionary.get("state_of_the_building", []) + [property.property_building_state]

    return property_data_dictionary


def write_data_to_file(property_data_dictionary):
    data_file = pd.DataFrame(property_data_dictionary,columns=columns)
    data_file.to_csv("Property_structured_data.csv")
