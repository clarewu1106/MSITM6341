# Name: Dongying Wu
# Student ID: 729678
# Due date: December 3nd, 2019
# Class: #MSITM 6341


class Rectangle():
    def __init__(self):
        self.height = 10
        self.width  = 8

    def print_dimensions(self):
        print("The dimensions of the rectangle are: " + str(self.width) + " x " + str(self.height))

    def get_area(self):
        area = self.height*self.width
        return area

    def get_perimeter(self):
        perimiter = (self.height*2)+(self.width*2)
        return perimiter

new_rectangle = Rectangle()
new_rectangle.print_dimensions()


print("the rectangle area is: " + str(new_rectangle.get_area()))

print("the rectangle perimeter is: " + str(new_rectangle.get_perimeter()))