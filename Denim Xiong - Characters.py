import random


class Character(object):
    def __init__(self, name, health, description, attack):
        self.name = name
        self.health = health
        self.description = description
        self.attack = attack
        self.death = False

    def take_damage(self, amount):
        self.health -= amount

    def hit(self, target):
        target.take_damage(self.attack)
        print('%s attacks %s for %s' % (self.name, target.name, self.attack))
        if target.health <= 0:
            target.death = True
            print('%s died.' % target.name)
            exit(0)

    def fight(self, enemy):
        print(you.name, ",", you.description, "Starts fighting with %s'" % bad.name, ",", bad.description)

        while self.health != 0:
            you.attack = random.randint(1, 10)
            bad.attack = random.randint(1, 10)
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.hit(self)
            elif choice == enemy:
                self.hit(enemy)


you = Character("Zeus", 100, "A useless old man.", "")
bad = Character("Bull Demon King", 100, "A giant, tough bull.", "")
you.fight(bad)
