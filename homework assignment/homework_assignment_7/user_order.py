# Name: Dongying Wu
# Student ID: 729678
# Due date: October 29, 2019
# Class: #MSITM 6341

menu = {
    "Chicken": 10,
    "Steak": 20,
    "Mashed potatoes": 5,
    "Sandwich": 10,
    "French Fries": 4,
    "Hambuger": 17
}

total = 0

while(True):
    order = input("Enter an item:")
    if order == 'N':
        break
    
    elif order in menu:
        itemPrice = menu.get(order)
        print ("{} : ${:.1f}".format(order,itemPrice))  
        total += itemPrice
    else:
        print ("We do not have {}".format(order))

print("----------------------")
print("Order Total: ${:.1f}".format(total))
    
