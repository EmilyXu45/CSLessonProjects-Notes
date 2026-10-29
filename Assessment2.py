# Question 1
# Creating a recursive_sum function

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return recursive_sum(n-1)+n
print(recursive_sum(3))

# Dictionary to first 10 recursive sums

Sums = {}
for i in range(1,11):
    # Assigning the value (recursive_sum(i)) to the key i
    Sums[i] = recursive_sum(i)
print(Sums)

# Mistake correction: this creates a set; dictionaries must use colon, sets are unordered which means that the numbers are arranged based on internal memory hashes rather than the order
# Difference between set & dictionaries: A set is a collection of unique values while a dictionary is collection of key value pairs.
'''
sums = {}
for i in range(1,11):
    sums = {i, recursive_sum(i)}
    print(sums)
'''

