# Name: Dongying Wu
# Student ID: 729678
# Due date: October 20, 2019
# Class: #MSITM 6341

menu = {
    "Chicken": 10,
    "Steak": 20,
    "Mashed potatoes": 5,
    "Sandwich": 10,
    "Hambuger": 17
}

total = 0
order = ['Chicken', 'Pork', 'Mashed potatoes']

for item in order:    
    if item in menu:
        itemPrice = menu.get(item)
        print ("{} : ${:.1f}".format(item,itemPrice))
        total += itemPrice
    else:
        print ("We do not have {}".format(item))

print("----------------------")
print("Order Total: ${:.1f}".format(total))
