#Name: Dongying Wu
#Student ID: 729678
#Due date: September 29, 2019
#Class: #MSITM 6341


menu_items_in_stock = ['Tacos','Chips','Salsa','Quesadilla']
customer_order = ['Tacos','Guacamole','Burrito','Chips', 'Salsa']

menu_items_in_stock = [element.lower() for element in menu_items_in_stock]
customer_order = [element.lower()for element in customer_order]
print ("Items in Stock:" +  str(menu_items_in_stock))
print ("Customer Order:" + str(customer_order))

if 'Tacos' not in menu_items_in_stock:
    print ("we have Tacos in stock")
else: 
    print ("we do not have Tacos in stock")
if 'Guacamole' not in menu_items_in_stock:
    print ("We do not have Guacamole in stock")
else:
    print ("we have Guacamole in stock")
if 'Burrito' not in menu_items_in_stock:
    print ("we do not have Burrito in stock")
else:
    print ("we have Burrito in stock")
if 'Chips' not in menu_items_in_stock:
    print ("we have Chips in stock")
else:
    print ("we do not have Chips in stock")
if 'Salsa' not in menu_items_in_stock:
    print ("we have Salsa in stock")
else:
    print ("we do not have Salsa in stock")