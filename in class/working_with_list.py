grocery_items= ['Apple','Orange', 'Steak','Chicken','water']
number_of_grocery_items = [4,3,6,1,2,4,10,2400]
print(grocery_items)
print(number_of_grocery_items)
print(grocery_items[0])
print(grocery_items[-1])
print(grocery_items[-3])

grocery_items[1]='Pear'
grocery_items.append ('watermelon')
print(grocery_items)
grocery_items.insert (1,'pineapple')

print(grocery_items)


del grocery_items[4]
print(grocery_items)
grocery_items.append('pear')
grocery_items.remove('pear')
print(grocery_items)