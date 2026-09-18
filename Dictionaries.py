# Dictionary = {"Key": "Value"}
# Dictionary keys are unique and immutable; they can be a string, number or a tuple (lists are mutable)
# Values are more flexible and can be a string, number, list or another dictionary
capitals = {"USA":"Washington D.C.", "France":"Paris"}
# Add key-value pair
capitals = {"Japan":"Tokyo"}

things = {
    # "Key": ["Value as a list"]
    "Fruit": ["Mango", "Banana"],
    "Color": "Yellow"
}

# get() can be used to return a default message when the key is not found; if the key is found, the value is returned
capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

country = input("Country: ")
capital = capitals.get(country, "Unknown country")
print(capital)

# loop through the dictionary so that each country and its capital is printed.
for country in capitals:
    print(country, "->", capitals[country])

# Updating values using keys
captains = {"England":"Root", "Australia":"Smith", "India":"Dhoni", "Srilanka":"Jayasurya"}

captains["India"] = "Virat"
captains["Australia"] = "Paine"
# delete a key-value pair using del
del captains["India"]
# pop() removed a key and returns its value, popitem() removes and returns the most recently inserted key-value pair
removed = captains.pop("Australia")

d1 = {'name': 'Steve', 'age': 21, 'marks': 60, 'course': 'Computer Engg'}
captains = {"England":"Root", "Australia":"Paine", "India":"Virat"}

# return the view of the keys and values as objects, where a list can be applied
print(d1.keys())
print(d1.values())

# check whether a key exists (not value)
print("India" in captains)

# Nested dictionary
students = {
    101: {'name': 'Steve', 'age': 25, 'marks': 60},
    102: {'name': 'Anil', 'age': 23, 'marks': 75},
    103: {'name': 'Asha', 'age': 20, 'marks': 70}
}

print(students[103]['marks'])

# Word frequencies

import string
# Initialise dictionary to store each unique work and their count
word_counts = {}

with open("romeo_juliet_sample.txt", "r") as file:
    text = file.read().lower()
# searches through the whole file, everytime a punctuation is found, it is replaced with a space for easier splitting
for mark in string.punctuation:
    text = text.replace(mark, " ")

words = text.split()

for word in words:
    # Count each new word
    if word not in word_counts:
        # Adding word to the dictionary (key and value)
        word_counts[word] = 1
    else:
        # Update the value for repeated words
        word_counts[word] = word_counts[word] + 1
# len(word_counts) totals the number of keys (unique words)
print("Different words:", len(word_counts))
# Get the value for the key "romeo" (or "juliet") if there is no word, return 0
print("romeo:", word_counts.get("romeo", 0))
print("juliet:", word_counts.get("juliet", 0))