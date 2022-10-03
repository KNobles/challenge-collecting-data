from collections import defaultdict
from selenium import webdriver

class Property:
    def __init__(self, property_url) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True 
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(property_url)
        property_data = self.property_data()

        self.property_type = property_data["property"]["type"]
        self.property_sub_type = property_data["property"]["subtype"]
        self.property_locality = property_data["property"]["location"]["locality"]
        self.property_sale_type = property_data["price"]["type"]
        self.property_price = property_data["price"]["mainValue"]
        self.property_room_count = property_data["property"]["bedroomCount"]
        self.property_surface = property_data["property"]["netHabitableSurface"]
        self.property_is_kitchen_fully_equipped = self.property_is_kitchen_fully_equipped()
        self.property_is_furnished = 1 if property_data["transaction"]["sale"]["isFurnished"] == True else 0
        self.porperty_has_open_fire = 1 if property_data["property"]["fireplaceExists"] == True else 0
        self.property_has_terrace = 1 if property_data["property"]["hasTerrace"] == True else 0
        self.property_has_garden = 1 if property_data["property"]["hasGarden"] == True else 0
        # MISSING SURFACE OF THE LAND AND THE SURFACE OF THE PLOT AREA, WILL DO IT
        self.property_facade_count = self.property_data()
        self.property_has_swimming_pool = 1 if property_data["property"]["hasSwimmingPool"] == True else 0
        # self.property_building_state = property_data["property"]["building"]["condition"]
    
    def some_test(self, data):
        try:
            newdata = data
        except TypeError:
            newdata = None
        return newdata


    def property_facade_count(self):
        try:
            facade_count = self.property_data()["property"]["building"]["facadeCount"]
        except TypeError:
            return None

    def property_data(self):
        return self.driver.execute_script("return window.classified")

    def property_is_kitchen_fully_equipped(self):
        try:
            has_kitchen = self.property_data()["property"]["kitchen"]["type"]
            if has_kitchen == "HYPER_EQUIPPED":
                return 1
            else:
                return 0
        except TypeError:
            return None

