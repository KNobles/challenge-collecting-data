from selenium import webdriver

class Property:

    def __init__(self, property_url) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True 
        driver = webdriver.Firefox(options=options)
        driver.get(property_url)
        property_data = driver.execute_script("return window.classified")
        self.property_type = property_data["property"]["type"]
        self.property_sub_type = property_data["property"]["subtype"]
        self.property_locality = property_data["property"]["location"]["locality"]
        self.property_sale_type = property_data["price"]["type"]
        self.property_price = property_data["price"]["mainValue"]
        self.property_room_count = property_data["property"]["bedroomCount"]
        self.property_surface = property_data["property"]["netHabitableSurface"]
        self.property_is_kitchen_fully_equipped = 1 if property_data["property"]["kitchen"]["type"] == "HYPER_EQUIPPED" else 0
        self.property_is_furnished = 1 if property_data["transaction"]["sale"]["isFurnished"] == True else 0
        self.porperty_has_open_fire = 1 if property_data["property"]["fireplaceExists"] == True else 0
        self.property_has_terrace = property_data["property"]["hasTerrace"]
        self.property_has_garden = property_data["property"]["hasGarden"]
        # MISSING SURFACE OF THE LAND AND THE SURFACE OF THE PLOT AREA, WILL DO IT
        self.property_facade_count = property_data["property"]["building"]["facadeCount"]
        self.property_has_swimming_pool = property_data["property"]["hasSwimmingPool"]
        self.property_building_state = property_data["property"]["building"]["condition"]