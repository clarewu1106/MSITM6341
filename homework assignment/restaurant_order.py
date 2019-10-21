# Name: Dongying Wu
# Student ID: 729678
# Due date: October 20, 2019
# Class: #MSITM 6341


import string
ALPHABET = string.ascii_uppercase

menu = [
    ("Pizza", 15),
    ("Hamburger",   20),
    ("Sandwitch", 13),
    ("Chicken", 10),
    ("Mashed Potatoes",5)
]

def print_menu(food_with_prices):
    for (index, (food, price)) in enumerate(food_with_prices):
        print("""\
 {letters} {food}:$ {price}  
""".format(letters=ALPHABET[index], food=food, price=price))

print_menu(menu)
total = 0
print("""
+-------------------------------------------+""")

while(True):
    print("Total:",total)
    x = input("Select a letter or 'done': ")
    if x in ALPHABET[:len(menu)]:
        total +=menu[ALPHABET.index(x)][1]
    elif x not in ALPHABET[:len(menu)]:
        print ("We do not have this item")
    elif x == 'done':
        break

print("You total is {}".format(total))
