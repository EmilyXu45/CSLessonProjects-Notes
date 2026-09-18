# https://jamesabela.github.io/jsfun/dictionaries_course/10_final_project.html
# Level 10 of 10 - Dictionaries

# Final project - Dictionary App
# Build your own dictionary-powered tool.
# Ideas:
# Country capital quiz
import random

capitals = {
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "Egypt": "Cairo",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
    "Malaysia": "Kuala Lumpur",
    "Mexico": "Mexico City",
    "Morocco": "Rabat",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Nigeria": "Abuja",
    "Norway": "Oslo",
    "Peru": "Lima",
    "Philippines": "Manila",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "Spain": "Madrid",
    "Thailand": "Bangkok",
    "Turkey": "Ankara",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Vietnam": "Hanoi"
}

score = 0
count = 0
lives = 3
print()
print("Country Capital Quiz 🌍")
print("-"*30)
print()
print("Guess the capital of the country! Type quit to end the game")

while True:
        Country = random.choice(list(capitals.keys()))
        Capital = capitals[Country]
        guess = input("Capital of "+ Country+": ")
        if guess.lower() == "quit":
            break
        elif guess == Capital:
            print ("Correct!")
            score += 1
            count +=1
        else:
            print ("Wrong!")
            count+=1
            lives -=1
            print(f"lives remaining: {lives}")

            if lives == 0:
                print("Game Over! You ran out of lives.")
                break
print()
print("-"*30)
print()
print (f"You scored: {score} out of {count}")
print()
print("-"*30)
print()
print("Project finished")