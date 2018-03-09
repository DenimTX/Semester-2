class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        print("You sell the %s for %d gold" % (self.name, self.money))


class Weapon(Item):
    def __init__(self, name, money, damage):
        super(Weapon, self).__init__(name, money)
        self.damage = damage

longsword = Weapon