import random


class Character(object):
    def __init__(self, name, health, description, attack, money):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False
        self.money = money

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


you = Character("Zeus", 100, "an old man", 10, 0)
demon = Character("Bull Demon King", 2000, "a giant, tough bull.", 100, 1000000)
turtle = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200)
turtle1 = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200)
tiger = Character("Tiger", 400, "a ferocious white tiger.", 40, 400)
minion = Character("Minion", 50, "a weak minion.", 5, 50)
minion1 = Character("Minion", 50, "a weak minion.", 5, 50)
minion2 = Character("Minion", 50, "a weak minion.", 5, 50)
minion3 = Character("Minion", 50, "a weak minion.", 5, 50)
minion4 = Character("Minion", 50, "a weak minion.", 5, 50)
minion5 = Character("Minion", 50, "a weak minion.", 5, 50)
minion6 = Character("Minion", 50, "a weak minion.", 5, 50)
minion7 = Character("Minion", 50, "a weak minion.", 5, 50)
minion8 = Character("Minion", 50, "a weak minion.", 5, 50)
minion9 = Character("Minion", 50, "a weak minion.", 5, 50)


# Denim Xiong
