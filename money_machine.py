class MoneyMachine:
    ''' Manages payments and profit record '''
    CURRENCY="$"
    COIN_VALUES={
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickels" : 0.05,
        "pennies" : 0.01,
    }

    def __init__(self):
        self.profit=0
        self.money_received=0

    def report(self):
        '''prints the currency report'''
        print(f"Money:{self.CURRENCY}{self.profit}")

    def process_coins(self):
        '''Retuens total value calculated from coins inserted'''
        print("Insert the coins")
        for coins in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coins}?:"))*self.COIN_VALUES[coins]

        return self.money_received

    def make_payment(self,cost):
        '''Returns True when payment is accepted false if insufficient'''
        self.process_coins()
        if self.money_received >= cost:
            change = round((self.money_received - cost), 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money, Money refunded!")
            self.money_received = 0
            return False

