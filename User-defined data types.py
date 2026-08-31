from enum import Enum

class CoffeeSize (Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

mySize = CoffeeSize.MEDIUM
print(mySize.value)
# prints the value 2
print(mySize.name)
#prints the label MEDIUM

# 3. Create my own enumerated types

#Task A -- Weather
class WeatherConditions (Enum):
    SUNNY = 1
    CLOUDY = 2
    RAINING = 3
    STORMY = 4
WeatherToday = WeatherConditions.RAINING
print("The weather today is: ", WeatherToday.name)
# Using enumerated types make the program more robust because:
# 1. Users can define their own data types to accept only certain values
# 2. Using pre-determined values ensures consistency throughout the program
# 3. fixed set number of values reduces the occurrences of invalid values/inputs.

# Example of class:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount


# Create two objects
account1 = BankAccount(owner="Alice", balance=1000)
account2 = BankAccount(owner="Bob",balance=500)

# Display information
print(account1.owner)
print(account1.balance)

# Deposit money
account1.deposit(200)

print(account1.balance)

# A class is used when the methods and operations carried out the data need to be stored as well.
# Compared to a record (which only stores the data), a class is more appropriate when the object has both an attribute and a method

# Task 6:

class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Woof Woof")

Dog1 = Dog(name="Milo", age=4)

print(Dog1.name)
print(Dog1.age)
Dog1.bark()

# Task 7: Independent Challenge: design a class

class Student:
    def __init__(self, name, year_group, average_mark):
        self.name = name
        self.year_group= year_group
        self.average_mark= average_mark
    def DisplayDetails(self):
        print("name: ", self.name)
        print("Year Group: ", self.year_group)
        print("Current Average Mark: ", self.average_mark)
    def UpdateMark(self, newmark):
        self.average_mark = newmark

student1= Student(name="Alice", year_group=12, average_mark=34)
student1.DisplayDetails()
student1.UpdateMark(56)
student1.DisplayDetails()