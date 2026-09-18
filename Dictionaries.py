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

