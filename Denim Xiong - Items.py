class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        print("You sell the %s for %s gold" % (self.name, self.money))

    def buy(self):
        print("You buy a %s." % self.name)


class Weapon(Item):
    def __init__(self, name, money, damage, lifesteal, description):
        super(Weapon, self).__init__(name, money)
        self.damage = damage
        self.lifesteal = lifesteal
        self.description = description


class Consumable(Item):
    def __init__(self, heal, name, money):
        super(Consumable, self).__init__(name, money)
        self.heal = heal
        self.name = name
        self.money = money

    def use(self):
        print("You drink a %s." % self.name)


class Armor(Item):
    def __init__(self, health, money):
        super(Armor, self).__init__('name', '1000')
        self.health = health
        self.money = money


longsword = Weapon('Longsword', 350, '25', 0, 'A generic longsword.\nDoes 25 damage')
vampiric_sword = Weapon('Vampiric Sword', 900, '15', 3, 'A mysterious sword that gives you 3 health when you attack '
                                                        'an enemy.\nDoes 15 damage.')
giant_sword = Weapon('Giant Sword', 1300, '50', 0, 'The sword of a giant.\nDoes 50 damage.')
excalibur = Weapon('Excalibur', 3600, '75', 0, 'A sword fit for a hero.\nDoes 75 damage.')


giant_hp_pot = Consumable(200, "Giant Health Potion", 100)
hp_pot = Consumable(100, "Health Potion", 50)


viking_helmet = Armor('350', 450)
thornmail = Armor('1000', 1100)
giants_belt = Armor('500', 600)
tabi_boots = Armor('200', 300)
cloth_armor = Armor('300', 400)
breastplate = Armor('400', 500)

# Denim Xiong
