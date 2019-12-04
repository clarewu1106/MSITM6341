class Restarant():

    def _init_(self):
        self.name = ""
        self.cuisine_type = ""
        self.menu = {}

    def add_menu_item(self,name,cost):
        self.menu[name] = cost

my_rest = Restarant()
my_rest.name = "McDonalds"
my_rest.cuisine_type = "Fast Food"

print(my_rest.name)

print(my_rest.name)

another_rest = Restarant
another_rest.name = "Chic Fil A"
another_rest.cuisine_type = "Fast Food"

print(another_rest.name)

my_rest.add_menu_item("French Fries", 2)
my_rest.add_menu_item("Hamberger", 4)
my_rest.add_menu_item("Milkshake", 3)

print(my_rest.menu)