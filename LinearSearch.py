# Declarations
list = [1,3,4,5,7]
search_item = int(input("What are you looking for: "))
found = False

for index in range (len(list)):
    if list[index] == search_item:
        found = True
        print(search_item, "found")
if found == False:
    print (search_item, "is not within list")

# O(N): the time taken to search through this list will increase linearly in proportion to n, the number of items in the data.
# For a linear search, the maximum number of searches would be n