'''
# Traversing linked list
data = ["ant", "bee", "cat", "dog", "elephant", "ferret", "giraffe"]
next_node=[4,1,2,6,3,5,-1]
start = 0

pointer = start #Start with the first item in the data list
while pointer != -1:
    print(data[pointer])
    pointer = next_node[pointer] #Update the pointer to point to the node of the data

# Adding to linked list
data = ["ant", "bee", "cat", "dog", ""]
next_node = [2, -1, 3, 1, -1]
start = 0
free = 4

# Put eel into the free node.
data[free] = "eel"

# Make eel point to the old start, then update start.
next_node[free] = 0
start = 4

pointer = start
while pointer != -1:
    print(data[pointer])
    pointer = next_node[pointer]
'''

data = ["ant", "bee", "cat", "dog"]
next_node = [2, -1, 3, 1]
start = 0
target = "dog"
found = False

pointer = start
while pointer != -1 and found == False:
    if data[pointer] == target:
        found = True
    else:
        pointer = next_node[pointer]

print("Found:", found)
print("Pointer:", pointer)