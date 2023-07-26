class CoffeeMaker:
    '''models the machine that makes a coffee'''
    def __init__(self):
        self.resources={
            "water":300,
            "milk":200,
            "coffee":150,

        }
    def report(self):
        '''prints a report of all available resources'''
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffee: {self.resources['coffee']}gm")

    def is_resource_sufficient(self, drink):
        ''' Returns True when order can be made, False if ingredients are insufficient '''
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}")
                can_make = False
                return can_make

        return can_make

    def make_coffee(self,order):
        '''Deducts the required ingredients from the resources'''
        for item in order.ingredients:
            self.resources[item] -= self.resources[item] - order.ingredients[item]
        print(f"Here is your {order.name},Enjoy!")




