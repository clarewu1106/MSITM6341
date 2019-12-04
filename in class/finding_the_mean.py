#find the mean of a list of numbers
#mean = sum of the numbers divided by how numbers they are

def mean(list_of_numbers):

    total = sum(list_of_numbers)
    count = len(list_of_numbers)
    return total / count


test_numbers = (5,32,8,19,24,42)

print(mean(test_numbers))