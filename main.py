from utils.url_scraper import Scraper
from utils.collect_property_data import Property

print("========================================================")
print("\tWELCOME TO THE COLLECTING DATA CHALLENGE")
print("========================================================\n")

# while True:
    # answer = input("Would you like to create a new set of data? [Y/n] ").lower()
    # if answer == "y":
        # Scraper.write_property_urls()
        # break
    # elif answer == "n":
        # break
    # else:
        # print("Answer needs to be [Y] or [n]\n")

prop = Property("https://www.immoweb.be/en/classified/duplex/for-sale/gent/9000/10143801?searchId=63399cae2b8c2")
print(vars(prop))
# print(prop.property_locality)
# print(prop.property_type)
# print(prop.property_sub_type)