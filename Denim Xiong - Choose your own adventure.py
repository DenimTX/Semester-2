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

    def fight(self, enemy):
        print(you.name, ",", you.description, "Starts fighting with %s'" % enemy.name, ",", self.description)

        while self.health != 0:
            choice = random.choice([enemy, self])
            if choice == self:
                enemy.hit(self)
            elif choice == enemy:
                self.hit(enemy)

    def sell(self):
        print("You sell the %s for %d gold" % (self.name, self.money))


your_inv = [""]
you = Character("Zeus", 100, "an old man", 10, 0, your_inv)
demon = Character("Bull Demon King", 2000, "a giant, tough bull.", 100, 1000000, ["Excalibur"])
turtle = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200, ["Longsword"])
turtle1 = Character("Turtle", 200, "a sturdy blue turtle.", 20, 200, ["Longsword"])
tiger = Character("Tiger", 400, "a ferocious white tiger.", 40, 400, ["Vampiric Sword"])
minion = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion1 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion2 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion3 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion4 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion5 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion6 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion7 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion8 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])
minion9 = Character("Minion", 50, "a weak minion.", 5, 50, ['Health Potion'])


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
        if self.name in your_inv:
            print("You sell the %s for %s gold" % (self.name, self.money))
            you.money += self.money
            your_inv.remove(self.name)
        else:
            print("You don't have a %s" % self.name)

    def buy(self):
        if you.money >= self.money:
            print("You buy %s." % self.name)
            you.money -= self.money
            your_inv.append(self.name)
        elif you.money < self.money:
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

    def use(self):
        if hp_pot or giant_hp_pot in your_inv:
            print("You drink a %s" % self.name)
            self.heal += you.health
        else:
            print("You don't have any consumables.")


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


class Room(object):
    def __init__(self, name, south, west, east, north, southwest, northeast, southeast, northwest, description):
        self.name = name
        self.south = south
        self.west = west
        self.east = east
        self.north = north
        self.southwest = southwest
        self.northeast = northeast
        self.southeast = southeast
        self.northwest = northwest
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


spawn_n = Room("Spawn (North)", None, None, None, None, None, None, "phoenix_n", None, 'You see a phoenix and a spawn '
                                                                                       'platform')
phoenix_n = Room("Phoenix (North)", None, None, None, None,
                 None, None, "phoenix_tower_intersection_n", "spawn_n", 'You see a path, a spawn platform, '
                                                                        'and a phoenix.')
phoenix_tower_intersection_n = Room("Phoenix-Tower Intersection (North)", "lane_high_middle", None, None, None,
                                    "mana_buff_camp_n", None, None, "phoenix_n", 'You see a turtle, a phoenix, and '
                                                                                 'a tower')
turtle_n = Room("Turtle Camp (North)", "bull_demon_king_intersection_n", None, None, None, None,
                "phoenix_tower_intersection_n", None, None, 'You see two paths and a turtle')
bull_demon_king_intersection_n = Room("Bull Demon King Intersection (North)", "bull_demon_king_intersection_s",
                                      "bull_demon_king", "lane_high_middle", "mana_buff_camp_n", None, None, None, None,
                                      'You see a turtle, a path, and a demon.')
lane_high_middle = Room("Lane High Middle", "lane_middle", "bull_demon_king_intersection_n", None,
                        "phoenix_tower_intersection_n", None, None, "tiger_camp", None,
                        'You see two paths, a tower, and a tiger.')
lane_middle = Room("Lane Middle", "lane_low_middle", None, "tiger_camp", "lane_high_middle", None, None,
                   None, None, 'You see two paths and a tiger.')
lane_low_middle = Room("Lane Low Middle", "phoenix_tower_intersection_s", "bull_demon_king_intersection_s", None,
                       "lane_middle", None, "tiger_camp", None, None, 'You see two paths, a tower, and a demon')
tiger_camp = Room("Tiger Camp", None, "lane_middle", None, None, "lane_low_middle", None, None,
                  "lane_high_middle", 'You see three paths and a tiger')
bull_demon_king_intersection_s = Room("Bull Demon King Intersection (South)", "mana_buff_camp", "bull_demon_king",
                                      "lane_low_middle", "bull_demon_king_intersection_n", None, None, None, None,
                                      'You see two paths, a turtle, and a demon')
bull_demon_king = Room("Bull Demon King", None, None, None, None, None, "bull_demon_king_intersection_n",
                       "bull_demon_king_intersection_s", None, 'You see two paths and a demon')
turtle_s = Room("Turtle Camp (South)", None, None, None, "bull_demon_king_intersection_s", None, None,
                "phoenix_tower_intersection_s", None, 'You see two paths and a turtle')
phoenix_tower_intersection_s = Room("Phoenix-Tower Intersection (South)", None, None, None, "lane_low_middle",
                                    "phoenix_s", None, None, "mana_buff_camp_s",
                                    'You see a tower, a phoenix, and a turtle.')
phoenix_s = Room("Phoenix (South)", None, None, None, None, "spawn_s", "phoenix_tower_intersection_s", None, None,
                 'You see a path, a spawn platform, and a phoenix.')
spawn_s = Room("Spawn (South)", None, None, None, None, None, "phoenix_s", None, None,
               'You see a spawn platform and a phoenix.')

current_node = spawn_n
directions = ['southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast']
short_directions = ['se', 'nw', 's', 'w', 'e', 'n', 'sw', 'ne']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_ ').lower().strip()
    if command == 'quit':
        exit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command == 'help':
        print("Type 'southeast', 'northwest', 'south', 'west', 'east', 'north', 'southwest', 'northeast', 'se', 'nw', "
              "'s', 'w', 'e', 'n', 'sw', 'ne' to move.")
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    elif command != 'inv' or 'inventory' or 'help' or 'quit':
        print("Command not found.")
    print("---------------------------------------------------------------------------------------------------------"
          "-----------------------------------------")
    print()
    you.fight(bull_demon_king)