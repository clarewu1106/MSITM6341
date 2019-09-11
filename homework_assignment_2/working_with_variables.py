# Name: Dongying Wu
# Student ID: 729678
# Due date: September 8, 2019
# Class: #MSITM 6341


# Variable of Stock Symbol
stock_symbol = "appl"
# Variable of Price
price = 204.66
# Variable of Change
change = 4.08
# Dollar Amount Calculation formula 
dollar_amount_changed = price - change

# Print Dollar Sign with Price
dollar_sign = '${}'.format(price)
# Limit Dollar Amount Changed with Two Decimal Numbers
two_decimal = "%.2f" % dollar_amount_changed


# Output_1
print ("Symbol:" + stock_symbol.upper() + ", " + "Price:" + str(price) + ", " + "Change:" + str(-change)) 
# Output_2
print ("Symbol:" + stock_symbol.lower() + ", " + "Price:" + str(dollar_sign) + ", " + "Change:" + str(-change))
# Output_3
print ("Symbol:" + stock_symbol.upper() + " --- " + "Yesterday's Price:" + str (two_decimal)) 

