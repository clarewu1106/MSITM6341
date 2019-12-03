# Name: Dongying Wu
# Student ID: 729678
# Due date: December 1, 2019
# Class: #MSITM 6341


def maximum_diff():
    
    n = []
    
    num = int(input("How many numbers? "))
    
    for i in range (0, num):
        
        ele = int(input())
        
        n.append(ele)
        
    abst = max(n) - min(n)
    print("Maxium diffference is: " + str(abst))
    
    

maximum_diff()