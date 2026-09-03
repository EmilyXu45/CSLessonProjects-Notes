# Level 10 of 10 - Files Course
# Tutorial: https://jamesabela.github.io/jsfun/files_course/10_monster_codex.html
#load https://raw.githubusercontent.com/jamesabela/Python-RPG-Tutorial/2efb37c62e8a34f9267d8f408b29d59298b4b2ca/Monsters.txt

# Creative Project: Monster Codex
# There are no direct tests for this level.
# Build something useful or fun using the loaded Monsters.txt file.
# Ideas:
# 1. Print every monster in a neat list.
# 2. Let the player search for a monster by name.
# 3. Save favourite monsters to favourites.txt.
# 4. Append battle notes to battle_log.txt.
# 5. Create a random monster encounter.

import random

print("Monster Codex")
print("Build your own RPG file project here!")

# Starter idea:
with open("Monsters.txt", "r") as monster_file:
    monsters = monster_file.readlines()

print("Loaded", len(monsters), "monster lines.")
print("Random encounter:")
print(random.choice(monsters))

while True:
    print("1. Print every monster")
    print("2. Search for monster")
    print("3. Save monster")
    print("4. Add battle notes")
    print("5. Random monster battle")
    print("6. Exit")
    Menu_choice = int(input("Enter your choice: "))
    if Menu_choice == 6:
        exit()

def Display_Monsters():
    with open("Monsters.txt", "r") as monster_file:
        monsters = monster_file.readlines()
        for monsters in monster_file:
            parts = line.strip().split(",")
            MonsterName = parts[1]
            print (MonsterName)

Display_Monsters()