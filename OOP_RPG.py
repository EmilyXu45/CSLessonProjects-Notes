# Part 1: Monsters into two separate arrays (One for computer, one for the user)
#   Create the cards
#   Load them into the arrays
# Part 2
#

# Initialise the game: ask the user how many rounds they want to play
# Initialise the lives_count to depending on the round, if round < 10, lives = 3, if lives > 10 and lives < 20 lives = 5, else lives = 7
# Check if lives is 0 or the number of cards remaining is 0:
    # If either condition is met, terminate the game
    # Continue the game

import random
import time

AllCards = []

Rounds = int(input("Enter how many round you want to play: "))
if Rounds < 10:
    lives = 3
elif Rounds > 10 and Rounds < 20:
    lives = 5
else:
    lives = 7

print("Starting game...")
time.sleep(2)
print("Generating your card... ")
time.sleep(2)

class Monsters:
    def __init__(self, Name, Attack, Defense, Power, Intelligence):
        self.name = Name
        self.attack = Attack
        self.defense = Defense
        self.power = Power
        self.intelligence = Intelligence

    def __repr__(self):
        return f" {self.name} \n ATTACK: {self.attack}\n DEFENSE: {self.defense}\n POWER: {self.power}\n INTELLIGENCE: {self.intelligence}"

def GenerateCards():
    try:
        with open ("OOPMonsters.txt", 'r') as file:
            lines = file.read().splitlines()
            for i in range(0,len(lines),5):
                name = lines[i]
                attack = lines[i+1]
                defense = lines[i+2]
                power = lines[i+3]
                intelligence = lines[i+4]

                Monster = Monsters(name, attack, defense, power, intelligence)
                AllCards.append(Monster)
    except OSError:
        print("File is not found!")

GenerateCards()

CardNo1 = random.randint(1, 30)
CardNo2 = random.randint(1,30)
if CardNo1 != CardNo2:
    UserCard = AllCards[CardNo1]
    ComputerCard = AllCards[CardNo2]
else:
    UserCard = AllCards[CardNo1]
    ComputerCard = AllCards[CardNo1+1]

def LoadCards():
    print("_"*20)
    print(UserCard)


LoadCards()

print("_"*20)

def DisplayMenu():
    print("1. ATTACK")
    print("2. DEFENSE")
    print("3. POWER")
    print("4. INTELLIGENCE")

DisplayMenu()

win = 0
loss = 0
while lives !=0 and Rounds !=0:
    Rounds -=1
    CardNo2 = random.randint(1, 29)
    ComputerCard = AllCards[CardNo2]
    Category = int(input("Choose a category: "))
    if Category == 1:
        if UserCard.attack > ComputerCard.attack:
            print("You win 🎉!!")
            win+=1
        else:
            print("The attack power of the computer's card is: ", ComputerCard.attack)
            print("The Monster is: ",ComputerCard.name)
            print("You lose!")
            lives -=1
    elif Category == 2:
        if UserCard.defense > ComputerCard.defense:
            print("You win 🎉!!")
            win += 1
        else:
            print("The defense power of the computer's card is: ", ComputerCard.attack)
            print("The Monster is: ",ComputerCard.name)
            print("You lose!")
            lives -= 1
            loss+=1
    elif Category ==3:
        if UserCard.power > ComputerCard.power:
            print("You win 🎉!!")
            win += 1
            loss += 1
        else:
            print("The power of the computer's card is: ", ComputerCard.attack)
            print("The Monster is: ",ComputerCard.name)
            print("You lose!")
            lives -= 1
    else:
        if UserCard.intelligence > ComputerCard.intelligence:
            print("You win 🎉!!")
            win += 1
            loss += 1
        else:
            print("The intelligence of the computer's card is: ", ComputerCard.attack)
            print("The Monster is: ",ComputerCard.name)
            print("You lose!")
            lives -= 1


print("_"*20)
print("Printing game stats... ")
time.sleep(2)
print(f"You have won {win} rounds")
print(f"You have lost {loss} rounds")

