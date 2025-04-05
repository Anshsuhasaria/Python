class trader1():
    def skills(self):
        print("options trading")

class trader2():
    def skills(self):
        print("forex trading")

class alpha_trader(trader1,trader2):
    def skills(self):
        trader1.skills(self)
        trader2.skills(self)
        print("futures")

a = alpha_trader()
a.skills()
