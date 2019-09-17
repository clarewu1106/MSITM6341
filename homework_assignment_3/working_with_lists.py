# Name: Dongying Wu
# Student ID: 729678
# Due date: September 15, 2019
# Class: #MSITM 6341

# Items & Price lists
grocery_store_items = ['soda','beer','milk','bread','cereal']
prices = [3.99,5.96,8.5,6.99,3.96]
print ("Items list:" , grocery_store_items)
print ("prices list:" , prices, "\n")

print ("************************(Question 1)***********************")
# 1. Print the 3rd item followed by it’s price
print((grocery_store_items[2]).title() + " price is: " + '${}'.format(prices[2])) 

print ("************************(Question 2)***********************")
# 2. Print the last item followed by it’s price
print ((grocery_store_items[-1]).title() + " price is: " + '${}'.format(prices[-1])) 

print ("**********************(Question 3,4,5)*********************")
# 3. Add a 6th item and it’s price
grocery_store_items.append('eggs'), prices.append(5.06)
# 4. Print the list of items
print (grocery_store_items)
# 5. Print the list of prices
print (prices)

print ("************************(Question 6)***********************")
# 6. Remove the first item and it’s price
del grocery_store_items[0]
del prices[0]
print (grocery_store_items)
print (prices)

print ("************************(Question 7)***********************")
# 7. Double the price of 2nd item
def double(prices):
    for prices[0] in prices:
        prices[1]*= 2
        return (prices)
print(double(prices))

print ("***********************(Question 8,9)**********************")
# 8. Print the list of items
print (', '.join(grocery_store_items).title())

# 9. Print the list of prices
prices1 = [str(a) for a in prices]
print(', ' .join(prices1))
