import random

print("Welcome to the Day Trip Generator!  With your input, this program will plan your perfect day trip... enjoy the experience!")
print(" ")
destination = ["Jamaica","Costa Rica","San Francisco","San Antonio","Milwaukee"]
restaurants = ["Just Natural","Rasta Aide","Paloma","Cattleman's Steakhouse","Lake Park Bistro"]
transportation = ["Uber", "Car", "Segway", "Bike", "Walking"]
entertainment = ["Zipline","Waterpark","Hiking","Shopping","Snorkling"]

# Destination Function

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

# Restaurant Function

def rest_options (restaurants):
    i = True
    while i == True:
            display_rest = random.choice(restaurants)
            rest_choice = input (f"How does {display_rest} sound for your restaurant today?: y/n  ").lower()
            if rest_choice == "n":
                 print ("Okay, let's try another restaurant option...")
            else:
                 print (f"Great choice, I love {display_rest}!")
                 i = False
    return rest_choice

# Transportation Options Function

#def trans_options (transporation):
 #    i==True

                 





final_dest = dest_options(destination)
print(" ")
final_rest = rest_options(restaurants)