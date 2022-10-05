import json
from selenium.webdriver.common.by import By
import requests
from requests import Session
from bs4 import BeautifulSoup
class Property:
    def __init__(self, json_obj) -> None:
        # print(json.loads(script.contents[0][33:-10])["property"]["subtype"])
        self.property_data = json_obj
        self.id = self.id()
        self.locality = self.locality()
        self.type = self.type()
        self.sub_type = self.sub_type()
        self.sale_type = self.sale_type()
        self.price = self.price()
        self.bedroom_count = self.bedroom_count()
        self.surface = self.surface()
        self.is_kitchen_fully_equipped = self.is_kitchen_fully_equipped()
        self.is_furnished = 1 if self.property_data["transaction"]["sale"]["isFurnished"] == True else 0
        self.has_open_fire = 1 if self.property_data["property"]["fireplaceExists"] == True else 0
        self.has_terrace = 1 if self.property_data["property"]["hasTerrace"] == True else 0
        self.has_garden = 1 if self.property_data["property"]["hasGarden"] == True else 0
        self.terrace_surface = self.property_data["property"]["terraceSurface"] if self.property_data["property"]["terraceSurface"] == True else "None"
        self.garden_surface = self.property_data["property"]["gardenSurface"] if self.property_data["property"]["gardenSurface"] == True else "None"
        self.land_surface = self.land_surface()
        self.facade_count = self.facade_count()
        self.has_swimming_pool = 1 if self.property_data["property"]["hasSwimmingPool"] == True else 0
        self.building_state = self.building_state()

    # def property_data(self, property_url):
    #     with Session() as sess:
    #         req = sess.get(property_url, timeout=3)
    #         soup = BeautifulSoup(req.content, "html.parser")
    #         script = soup.find('script',attrs={"type" :"text/javascript"})
    #     return json.loads(script.contents[0][33:-10])
    
    def id(self):
        property_id = self.property_data["id"]
        return property_id

    def surface(self):
        surface = self.property_data["property"]["netHabitableSurface"]
        if surface is None:
            surface = "None"
        return surface

    def price(self):
        price = self.property_data["price"]["mainValue"]
        if price is None:
            price = "None"
        return price

    def sale_type(self):
        sale_type = self.property_data["price"]["type"]
        if sale_type is None:
            sale_type = "None"
        return sale_type
    
    def sub_type(self):
        sub_type = self.property_data["property"]["subtype"]
        if sub_type is None:
            sub_type = "None"
        return sub_type

    def type(self):
        type = self.property_data["property"]["type"]
        if type is None:
            type = "None"
        return type

    def locality(self):
        locality = self.property_data["property"]["location"]["locality"]
        if locality is None:
            locality = "None"
        return locality

    def bedroom_count(self):
        bedroom_count = self.property_data["property"]["bedroomCount"]
        if bedroom_count is None:
            bedroom_count = "None"
        return bedroom_count

    def land_surface(self):
        try:
            land_surface = self.property_data["property"]["land"]["surface"]
        except TypeError:
            land_surface = "None"
        return land_surface

    def building_state(self):
        try:
            building_state = self.property_data["property"]["building"]["condition"]
        except TypeError:
            building_state = "None"
        return building_state

    def facade_count(self):
        try:
            facade_count = self.property_data["property"]["building"]["facadeCount"]
        except TypeError:
            facade_count = "None"
        return facade_count

    def is_kitchen_fully_equipped(self):
        try:
            has_kitchen = self.property_data["property"]["kitchen"]["type"]
            if has_kitchen == "HYPER_EQUIPPED":
                return 1
            else:
                return 0
        except TypeError:
            return "None"