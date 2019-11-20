# Name: Dongying Wu
# Student ID:729678
# Due Date: 11/19/19
# MSITM 6341



def clamp(value, min, max):
    if value < min:
        return min
    elif max < value:
        return max
    else:
        return value
    
print(clamp(21, 45, 96))