import random


class Character(object):
    def __init__(self, name, health, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.money = money
        self.inventory = inventory

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if target.health <= 0:
            target.death = True
            print('%s died.' % target.name)
            print('You received %s gold.' % target.money)
            self.money += target.money
            exit(0)

    def fight(self, enemy):
        print(you.name, ",", you.description, "Starts fighting with %s'" % demon.name, ",", demon.description)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.hit(self)
            elif choice == enemy:
                self.hit(enemy)

    def sell(self):
        print("You sell the %s for %d gold" % (self.name, self.money))


your_inv = []
you = Character("Zeus", 100, "an old man", 10, 0, your_inv)
demon = Character("Bull Demon King", 2000, "a giant, tough bull.", 100, 1000000, "")
turtle = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200, "")
turtle1 = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200, "")
tiger = Character("Tiger", 400, "a ferocious white tiger.", 40, 400, "")
minion = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion1 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion2 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion3 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion4 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion5 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion6 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion7 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion8 = Character("Minion", 50, "a weak minion.", 5, 50, "")
minion9 = Character("Minion", 50, "a weak minion.", 5, 50, "")


class Character(object):
    def __init__(self, name, health, description, attack, money, inventory):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.money = money
        self.inventory = inventory


class Item(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def sell(self):
        print("You sell the %s for %s gold" % (self.name, self.money))
        you.money += self.money

    def buy(self):
        if you.money >= self.money:
            print("You buy %s." % self.name)
            you.money -= self.money
        else:
            print("You don't have enough money.")


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

    def drink_health(self):
        if hp_pot in you.inventory:
            print("You drink a health potion.")
            you.health += hp_pot.heal
        else:
            print("You don't have a health potion.")

    def drink_big_health(self):
        if giant_hp_pot in you.inventory:
            print("You drink a giant health potion.")
            you.health += giant_hp_pot.heal
        else:
            print("You don't have a giant health potion.")


class Armor(Item):
    def __init__(self, health, money):
        super(Armor, self).__init__('name', '1000')
        self.health = health
        self.money = money


longsword = Weapon('Longsword', 350, 25, 0, 'A generic longsword.\nDoes 25 damage')
vampiric_sword = Weapon('Vampiric Sword', 900, 15, 3, 'A mysterious sword that gives you 3 health when you attack '
                                                      'an enemy.\nDoes 15 damage.')
giant_sword = Weapon('Giant Sword', 1300, 50, 0, 'The sword of a giant.\nDoes 50 damage.')
excalibur = Weapon('Excalibur', 3600, 75, 0, 'A sword fit for a hero.\nDoes 75 damage.')


giant_hp_pot = Consumable(200, "Giant Health Potion", 100)
hp_pot = Consumable(100, "Health Potion", 50)


viking_helmet = Armor(350, 450)
thornmail = Armor(1000, 1100)
giants_belt = Armor(500, 600)
tabi_boots = Armor(200, 300)
cloth_armor = Armor(300, 400)
breastplate = Armor(400, 500)

# Denim Xiong
