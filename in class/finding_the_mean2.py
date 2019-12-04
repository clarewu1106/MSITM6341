#write a function to find the median of a list of numbers

#Median = the median or central number in the list
# If odd number of values is the number in the middle
# else median is the average of the two cental number

def median(list_of_numbers):
    list_of_numbers.sort()
    count = len(list_of_numbers)
#check if 'count' is even or not
    if count % 2 == 0:
     first_idx = int(count / 2)  
     second_idx = first_idx - 1
     avg = (list_of_numbers[first_idx] + list_of_numbers[second_idx]) / 2
     return avg 

    else:
        middle_idx = count // 2
        return list_of_numbers[middle_idx]


odd_numbers = [12,13,13,7,5]
even_numbers = [12,32,7,9,12,14]

print(median(odd_numbers))
print(median(even_numbers))



