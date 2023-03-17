import random

print("Welcome to the Day Trip Generator!  With your input, this program will plan your perfect day trip... enjoy the experience!")

destination = ["Jamaica","Costa Rica","San Francisco","San Antonio","Milwaukee"]
restaurants = ["Just Natural","Rasta Aide","Paloma","Cattleman's Steakhouse","Lake Park Bistro"]
transportation = ["Uber", "Car", "Segway", "Bike", "Walking"]
entertainment = ["Zipline","Waterpark","Hiking","Shopping","Snorkling"]

def dest_options (destination):
    i = True
    while i == True:
        dest_choice = input(f"How does {random.choice(destination)} sound for your destination?: y/n  ").lower()
        if dest_choice == "n":
            print ("Okay, let's try again.")
        else:
            print("Great, let's move on to the next feature of your trip!")       
            i = False
    return dest_choice

final_dest = dest_options(destination)