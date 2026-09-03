# Level 10 of 10 - Files Course
# Tutorial: https://jamesabela.github.io/jsfun/files_course/10_monster_codex.html
#load https://raw.githubusercontent.com/jamesabela/Python-RPG-Tutorial/2efb37c62e8a34f9267d8f408b29d59298b4b2ca/Monsters.txt

# Creative Project: Monster Codex
# There are no direct tests for this level.
# Build something useful or fun using the loaded Monsters.txt file.
# Ideas:
# 5. Create a random monster encounter.


import random

print("Monster Codex")
print("Build your own RPG file project here!")

def Process_complete():
    print ()
    print ("-"*20)
    print()

# 1. Print every monster in a neat list.
def Display_Monsters():
    with open("Monsters.txt", "r") as monster_file:
        next (monster_file) # Skip the name title
        print("-"*20)
        print("Displaying All Monsters:")
        print()
        for line in monster_file:
            parts = line.strip().split(",")
            if len(parts) > 1:
                MonsterName = parts[1]
                print(MonsterName)
        Process_complete()

# 2. Let the player search for a monster by name.
def Find_Monster(Monster):
    found = False
    with open("Monsters.txt", "r") as monster_file:
        for line in monster_file:
            parts = line.strip().split(",")
            Name = parts[1]
            Nationality = parts[2]
            Description = parts[3]
            if Monster == Name:
                print("Monster Found!")
                print(Name, "is a", Nationality, "monster;", "they are", Description)
                found = True
    if found == False:
        print("Monster NOT found!!")
    Process_complete()

# 3. Save favourite monsters to favourites.txt.
def Fav_Monsters(Monster):
    with open("favourites.txt", "a") as favourites_file:
     favourites_file.write(Monster)
     favourites_file.write("\n")
    Process_complete()

# 4. Append battle notes to battle_log.txt.
def Battle_Notes(Battle):
    with open("Battles.txt", "a") as battles_file:
     battles_file.write(Battle)
     battles_file.write("\n")
    Process_complete()

# 5.Create a random monster encounter

def Monster_Attack():
    found = False
    # User picks their monster by name
    MonsterChoice = input ("Enter the name of your monster: ")
    with open("Monsters.txt", "r") as monster_file:
        for line in monster_file:
            parts = line.strip().split(",")
            Name = parts[1]
            if MonsterChoice == Name:
                MonsterForce1 = int(parts[4])
                MonsterDefence1 = int(parts[5])
                Choicetotalpower = int(parts[4]) + int(parts[5])
                found = True
                break
    if found == False:
        print("Monster NOT found!!")
        return

    with open("Monsters.txt", "r") as monster_file:
        next (monster_file)
        # Strips any spaces/empty lines, group monster descriptions and add them to a list Monster
        Monster = [line.strip() for line in monster_file if line.strip()]
        # Algorithm randomly picks a monster
        if Monster:
            random_monster = random.choice(Monster)
            parts = random_monster.split(",")
            monster_name = parts[1]
            # Output the monster picked by the machine
            print ("The machine has picked: ", monster_name)
            print("-" * 20)
            MonsterForce2 = int(parts[4])
            MonsterDefence2 = int(parts[5])
            Randomtotalpower = int(parts[4]) + int(parts[5])
            # Battle: Compare force & Defense of both
            # Output which on is stronger (+ stats)
            print("User's choice: ", Name, "has a power of", MonsterForce1)
            print("Computer's choice: ", monster_name, "has a power of", MonsterForce2)
            if MonsterForce1 > MonsterForce2:
                print(Name, "is more powerful")
            else:
                print(monster_name,"is more powerful")

            print("User's choice: ", Name, "has a defense of", MonsterDefence1)
            print("Computer's choice: ", monster_name, "has a defense of", MonsterDefence2)
            if MonsterDefence1 > MonsterDefence2:
                print(Name, "is stronger at defense")
            else:
                print(monster_name, "is stronger at defense")
            # Compare total of both monsters
            # Output the winner of the battle
            if Choicetotalpower > Randomtotalpower:
                print(Name, "is stronger overall!")
                print("-" * 20)
                print ("You win!")
            else:
                print(monster_name, "is stronger overall")
                print("-" * 20)
                print("You lose!")
    Process_complete()

def Menu():
    while True:
        print("1. Print every monster")
        print("2. Search for monster")
        print("3. Save monster")
        print("4. Add battle notes")
        print("5. Random monster battle")
        print("6. Exit")
        Menu_choice = int(input("Enter your choice: "))
        if Menu_choice ==1:
            Display_Monsters()
        elif Menu_choice ==2:
            Monster = input("Enter the name of the monster you are searching for: ")
            Find_Monster(Monster)
        elif Menu_choice ==3:
            Fav=input("Enter the name of your favourite monster: ")
            Fav_Monsters(Fav)
        elif Menu_choice == 4:
            Battle = input ("Enter battle notes")
            Battle_Notes((Battle))
        elif Menu_choice ==5:
            Monster_Attack()
        else:
            exit()

Menu()

