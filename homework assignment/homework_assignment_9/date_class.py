# Name: Dongying Wu
# Student ID: 729678
# Due date: November 24, 2019
# Class: #MSITM 6341

class date(): 
    
    def init(self):   
        self.day = ""
        self.month = ""
        self.year = ""

    def print_date(self):    
        print (self.month + " " +str(self. day)+", "+ str(self. year))

    def change_date(self,day,month,year):  
        self.day= day
        self.month = month
        self.year = year

dates = date()

dates.day = 19    
dates.month = "June"
dates.year= 2019

dates.print_date()    
dates.change_date (3, "August",2020)   
dates.print_date ()
