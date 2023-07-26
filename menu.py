class MenuItem:
    ''' models each menu item'''

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
                }
class Menu:
    ''' models menu with drink'''

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=50, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_item(self):
        '''Returns names of all available menu items'''

        options=" "
        for item in self.menu:
            options+=f"{item.name}/"
        return options

    def find_drink(self,order_name):
        " Searches the menu item for a particular drink,returns that item else returns none"
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f" sorry {order_name} is not available!")


