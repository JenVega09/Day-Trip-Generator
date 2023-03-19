import random

print("Welcome to the Day Trip Generator!  With your input, this program will plan your perfect day trip... enjoy the experience!")
print(" ")
destination = ["Jamaica","Costa Rica","San Francisco","San Antonio","Milwaukee"]
restaurants = ["Just Natural","Rasta Aide","Paloma","Cattleman's Steakhouse","Lake Park Bistro"]
transportation = ["Uber", "Car", "Segway", "Bike", "Walking"]
entertainment = ["Zipline","Waterpark","Hiking","Shopping","Snorkling"]
final_day_trip = {"destination":"","restaurants":"","transportation":"","entertainment":""}

# Destination Function

def dest_options (destination):
    i = True
    while i == True:
        display_dest_choice = random.choice(destination)
        dest_choice = input(f"How does {display_dest_choice} sound for your destination?: y/n  ").lower()
        if dest_choice == "n":
            print ("Okay, let's try another option...")
            print (" ")
        else:
            print(f"Great choice, I love {display_dest_choice} too!")
            print (" ")       
            i = False
    return display_dest_choice

# Restaurant Function

def rest_options (restaurants):
    i = True
    while i == True:
            display_rest = random.choice(restaurants)
            rest_choice = input (f"How does {display_rest} sound for your restaurant today?: y/n  ").lower()
            if rest_choice == "n":
                 print ("Okay, let's try another restaurant option...")
                 print (" ")
            else:
                 print (f"Great choice, I love {display_rest}!")
                 print (" ")
                 i = False
    return display_rest

# Transportation Options Function

def trans_options (transportation):
    i = True
    while i == True:
        display_trans=random.choice(transportation)
        trans_choice = input(f"Does using {display_trans} transportation work for you today?: y/n  ").lower()
        if trans_choice == "n":
            print("Okay, let's try another transportation option for you today...")
            print (" ")
        else:
            print(f"Great chioice, I also enjoy {display_trans} while I'm vacationing!")
            print (" ")
            i = False
    return display_trans

def enter_options(entertainment):
    i = True
    while i == True:
        display_enter = random.choice(entertainment)
        enter_choice = input(f"Does {display_enter} sound like fun to do today?: y/n  ").lower()
        if enter_choice == "n":
            print ("Okay, let's look at another fun activitiy to do today...")
            print (" ")
        else:
            print (f"Great choice, {display_enter} sounds like a blast!")
            print (" ")
            i = False
    return display_enter                   

# final_dest = dest_options(destination)
# final_rest = rest_options(restaurants)
# final_trans = trans_options(transportation)
# final_enter = enter_options(entertainment)

final_day_trip["destination"] = dest_options(destination)
final_day_trip["restaurants"] = rest_options(restaurants)
final_day_trip["transportation"] = trans_options(transportation)
final_day_trip["entertainment"] = enter_options(entertainment)

print (f"Looks like you will be using {final_day_trip['transportation']} to explore {final_day_trip['destination']}, eating dinner at {final_day_trip['restaurants']} and {final_day_trip['entertainment']} for fun.")
