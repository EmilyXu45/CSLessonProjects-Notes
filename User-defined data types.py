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



