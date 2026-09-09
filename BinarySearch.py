"""
Binary Vs Linear Search
Code to generate a list of numbers then perform a binary and a linear search.
You will be able to see the performance difference.
Look carefully, the Linear search is performing very well right now, so
why does everyone recommend a Binary Search?
How could you make this a fairer comparison?
"""
'''
from random import randint
import datetime

my_list = []

def list_generator(size):
    for i in range(size):
        new_num = randint(0,1000)
        while new_num in my_list:
            new_num = randint(0,1000)
        my_list.append(new_num)
    my_list.sort() #Sorting the list so that binary search can be performed

def linear_search (my_list, find_me):
    for i in range (len(my_list)):
        if my_list[i] == find_me:
            return i
    return False

def binary_search(my_list, find_me):
    l=0
    r = len(my_list)-1
    while l <= r:
        mid = l + (r - l) // 2
        # print('Check',mid) #You can use this to see the positions move
        # Check if find_me is present at mid
        if my_list[mid] == find_me:
            return mid

        # If find_me is greater, ignore left half
        elif my_list[mid] < find_me:
            l = mid + 1

        # If find_me is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return False

list_generator(900) # Generates a list for you to test against, lets put in 900 numbers
print("List Generated")
print(my_list)

num_to_find = 999 #Searching for number 50 and number 999 makes a difference

# See how well the binary search performs
print("\nBinary Search")
start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
print("position",binary_search(my_list, num_to_find)) #Change the number to what you want to check
time_taken = datetime.datetime.now() - start_time  # Current time - start time
print(time_taken)  # Printing the time it took

# See how well the linear search performs
print("\nLinear Search")
start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
print("position",linear_search(my_list, num_to_find))
time_taken = datetime.datetime.now() - start_time  # Current time - start time
print(time_taken)  # Printing the time it took
'''

list = [1,2,3,4,5,6,7,8,9]
# Sorted list
low = 0
# First index
high = len(list)-1
# low and high indicates the index of the element in the list, index starts on 0

#Binary search
found = False
search_value = int(input("Value to search for: "))
while found == False and low <= high:
    # when low <= high: there are still items in between
    middle = (high + low) // 2
    # Floor division to obtain an integer
    # In the loop so that the middle changes each time
    if list[middle] == search_value:
        found = True
    elif search_value < list[middle]:
        high = middle -1
    else:
        low = middle +1
        # Eliminate half of the list
if found == True:
    print ("found")
else:
    print("Not found")
# Olog(N) complexity because the search space is halved each time
# log (N) is the maximum number of comparisons
# The time taken to search for an item increases linearly as the number of items increases exponentially
