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
        display_dest_choice = random.choice(destination)
        dest_choice = input(f"How does {display_dest_choice} sound for your destination?: y/n  ").lower()
        if dest_choice == "n":
            print ("Okay, let's try another option...")
            print (" ")
        else:
            print(f"Great choice, I love {display_dest_choice} too!")
            print (" ")       
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


# def trans_options (transporation):
 #    i==True

                 





final_dest = dest_options(destination)
print(" ")
final_rest = rest_options(restaurants)
print (" ")
final_trans = trans_options(transportation)