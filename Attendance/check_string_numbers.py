# Name: Dongying Wu
# Student ID:
# Due Date: 11/05/19
# MSITM 6341

def compare_num(num1, num2): 
      
    n1 = num1.split(".") 
    n2 = num2.split(".") 
  
    i = 0 

    while(i < len(n1)): 
          
        if int(n2[i]) > int(n1[i]): 
            return -1
          
        if int(n1[i]) > int(n2[i]): 
            return 1
  
        i += 1
        
    return 0
  
# Run
number_1 = "15"
number_2 = "20"
  
result =  compare_num(number_1, number_2) 
if result < 0: 
    print (number_1 + " Smaller")
elif result > 0: 
    print (number_2 + " Smaller")
else: 
    print ("Equal")
