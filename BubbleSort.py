'''
list= [1,4,5,2,3,15,98]

for pass_num in range(len(list)):
    for index in range(len(list)-1):
    # len(list) -1 to ensure that the final index is still within the index numbers of the list
        if list[index]>list[index+1]:
            temp = list[index]
            list[index]=list[index+1]
            list[index+1]= temp
print (list)
'''

list= [1,4,5,2,3,15,98]
swapped = False

for pass_num in range (len(list)):
    swapped = False

    for index in range(len(list)-1-pass_num):
        if list[index] > list[index + 1]:
            temp = list[index]
            list[index] = list[index + 1]
            list[index + 1] = temp
            swapped = True

    if not swapped:
    # no swaps have been made in a full pass
        break
        # break out of the loop for the passes
print(list)