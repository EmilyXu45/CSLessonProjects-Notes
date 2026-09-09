list = [1,4,3,6,7,5]

for index in range (1, len(list)):
    key = list [index]
    j = index -1
    while j >= 0 and list[j]>key:
        list [j+1] = list[j]
        j= j-1
    list[j+1]=key
    # Idk why this works, help 😭
print(list)

# Descending
for index in range (1, len(list)):
    key = list [index]
    j = index -1
    while j >= 0 and list[j]<key:
        list [j+1] = list[j]
        j= j-1
    list[j+1]=key
print(list)

# Time complexity: O(N^2), cuz' of double loop?