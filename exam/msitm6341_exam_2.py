# Name: Dongying Wu
# Student ID: 729678
# Due date: November 12, 2019
# Class: #MSITM 6341
#
#
######################## Instructions ############################
#
# 1. Resolve any compiler errors
# 2. Follow any instructions given in comments starting with TODO
# 3. Resolve any runtime errors
# 4. Resolve any logical errors until the program outputs EXACTLY as the sample output below shows
#
##################### Program Description ########################
#
# The following program allows the admin of the Everest online
# store to enter new items to be added to the stores catalog.
# Once the user is done the program prints out a summary of 
# the new items that have been added.
#
############## Sample Output of Functioning Program ##############
#
# -------------------------------------------------------
# ---------------- Everest Admin Tool -------------------
# -------------------------------------------------------
# Welcome to the Everest admin tool!
# Here you will be able to add new items to the Everest
# online store and review the new addition(s) once you are done
# -------------------------------------------------------
# Enter an item name or 'done' when finished: Nintendo Switch
# Item price: 299.99
# Description: Excellent console developed by Nintendo
# Enter an item name or 'done' when finished: Apple iPhone
# Item price: 999.99
# Description: The newest phone in the Apple smartphone line up
# Enter an item name or 'done' when finished: Beats Studio 3
# Item price: 349.99
# Description: Over the ear headphones by Beats
# Enter an item name or 'done' when finished: DONE
# -------------------------------------------------------
# ---------------------- Summary ------------------------
# -------------------------------------------------------
# Nintendo Switch: $299.99 --- Desccription: Excellent console developed by Nintendo
#
# Apple iPhone: $999.99 --- Desccription: The newest phone in the Apple smartphone line up
#
# Beats Studio 3: $349.99 --- Desccription: Over the ear headphones by Beats



def print_item(item):
    #Need fix it
    #for item in list_of_store_items[]  
    print("{0}: ${1} --- Desccription: {2}".format(['name'], ['price'], ['description']))
    print("")
    



print("-------------------------------------------------------")
print("---------------- Everest Admin Tool -------------------")
print("-------------------------------------------------------")
print("Welcome to the Everest admin tool!")
print("Here you will be able to add new items to the Everest")
print("online store and review the new addition(s) once you are done")
print("-------------------------------------------------------")

list_of_store_items = {
    "Nintendo Switch": 299.99,
    "Apple iPhone": 999.99,
    "Beats Studio 3": 349.99,
}

while True:

    user_input = input("Enter an item name or 'done' when finished: ")

    if user_input == 'done':
        break
    else:
        price = input("Item price: ")
        description = input("Description: ")

        #TODO Implement the make_item function. This function should return a dictionary that
        #works correctly with the print_item function that has been defined for you.
        def make_item(name,price,description):
            new_item = make_item(user_input, float(price), description)
            list_of_store_items.append(new_item)
            return {'name':name,'price':price,'description':description}

print("-------------------------------------------------------")
print("---------------------- Summary ------------------------")
print("-------------------------------------------------------")

for item in list_of_store_items.items():
    print_item(item)
