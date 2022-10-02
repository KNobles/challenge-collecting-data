from utility.url_scraper import Scraper

print("========================================================")
print("\tWELCOME TO THE COLLECTING DATA CHALLENGE")
print("========================================================\n")

while True:
    answer = input("Would you like to create a new set of data? [Y/n] ").lower()
    if answer == "y":
        Scraper.write_property_urls()
        break
    elif answer == "n":
        break
    else:
        print("Answer needs to be [Y] or [n]\n")

