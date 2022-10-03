from selenium import webdriver

class Property:
    def __init__(self, property_url) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True 
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(property_url)
        self.property_data = self.property_data()

        self.locality = self.property_data["property"]["location"]["locality"]
        self.type = self.property_data["property"]["type"]
        self.sub_type = self.property_data["property"]["subtype"]
        self.sale_type = self.property_data["price"]["type"]
        self.price = self.property_data["price"]["mainValue"]
        self.bedroom_count = self.property_data["property"]["bedroomCount"]
        self.surface = self.property_data["property"]["netHabitableSurface"]
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

    def property_data(self):
        return self.driver.execute_script("return window.classified")

    def is_kitchen_fully_equipped(self):
        try:
            has_kitchen = self.property_data["property"]["kitchen"]["type"]
            if has_kitchen == "HYPER_EQUIPPED":
                return 1
            else:
                return 0
        except TypeError:
            return "None"

