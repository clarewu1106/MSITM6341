# Name: Dongying Wu
# Student ID: 729678
# Due date: September 22, 2019
# Class: #MSITM 6341


# Number Lists 3-50:
num_list = list(range(3,51))

# Comprehension to generate a list of odd numbers from 3 to 50
odd_numbers = [num for num in num_list if num % 2 == 1] 
print(odd_numbers)

# For loop, print first 5 odd number on single line.
for i in odd_numbers:
    if i in range(3,12):
       print(i) 
