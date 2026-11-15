# Class is the blueprint
# Object is a specific example
# Method is a function inside the Class

class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Character:
    # __init__ is the constructor: it sets up the initial state of an object by assigning values to its data attributes.
    def __init__(self, name, weapon):
        # name is an example of an attribute
        self.name = name
        # Creating a private attribute using .__
        self.__health = 50
        self.weapon = weapon

    # print_basics is a method
    def print_basics(self):
        print("Name:", self.name)

    def print_me(self):
        print(self.name, "is an adventurer")

    # A getter returns a private value while a setter changes a private value

    def get_health(self):
        return self.__health
    def set_health(self, new_health):
        self.__health = new_health

    def attack(self):
        print(self.name, "attacks with", self.weapon.name)
        print("Damage:", self.weapon.damage)


# Inheritance: Wizard inherits all the attributes from Character
class Wizard(Character):
    # Need to initialise again if there are additional attributes that belongs to Wizards only
    def __init__(self):
        # Inherits all attributes from Character
        Character.__init__()
        # New attribute: Not all characters have but wizards have
        self.magic = 30
    # Polymorphism: print_me is used for both characters and wizards class and it is the same method but it behaves differently
    # print_me in the child class overrides the one in the parent class as the child class is called first
    def print_me(self):
        print(self.name, "is a wizard")


# Multiple instances/ objects
arthur = Character("Arthur", "sword")
merlin = Character("Merlin", "knife")

print(arthur.name)
print(merlin.name)

arthur.set_health(88)
Arthurhealth = arthur.get_health()
print (Arthurhealth)

sword = Weapons("sword", 25)
# Containment: when an object of one class holds a reference to an object of another class.
# Hero's class is Character, it holds sword which an object of class Weapons
# The object Sword can exist independently too
hero = Character("Arthur", sword)
hero.attack()

class Monster:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def print_me(self):
        print(self.name, "attack", self.attack)

monster_data = [["Goblin", 12], ["Dragon", 99], ["Slime", 4]]
monster_collection = []

# The for loop iterates through each sub-list (e.g., ["Goblin", 12]).
for data in monster_data:
    # Monster(data[0], data[1]) unpacks those values, triggers the __init__ constructor and creates a brand-new Monster object.
    monster_collection.append(Monster(data[0], data[1]))

# The final loop iterates through the list of objects and calls the .print_me() method on each one.
for monster in monster_collection:
    monster.print_me()

class Monster2:
    def __init__(self, id, Name, Origin, Description, Attack, Magical_Force, Magical_Defence, Defence, Intelligence, Health):
        self.id = id
        self.Name = Name
        self.Origin = Origin
        self.Description = Description
        self.Attack = Attack
        self.Magical_Force = Magical_Force
        self.Magical_Defence = Magical_Defence
        self.Defence = Defence
        self.Intelligence = Intelligence
        self.Health = Health

    def __repr__(self):
        return self.Name


monster_collection2 = []

#Adding a monster to the list
monster_collection2.append(Monster2(1, "Bog Monster", "The bogs of Lincolnshire",
    "A foul monster that sucks people down into the bog!", 75, 12, 15, 65, 12, 99))

# Prints only the name of the monster because of __repr__ method in Monster2
# self = monster_collect[0]
print(monster_collection2[0])

import os

def read_monsters():
    try:
        with open('Monsters.txt') as f:
            for line in f:
                parts = line.split(",")
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory.")
        print("The current directory is", os.getcwd())

