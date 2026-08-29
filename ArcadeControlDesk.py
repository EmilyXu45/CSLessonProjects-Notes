print("Arcade Control Desk")
print("-"*20)

# Build a creative project using three list-based ADTs.
# 1. Stack: admin undo list
# 2. Queue: player waiting list
# 3. Linked list: quest chain using data and next lists
# 4. Menu: let the user choose operations

print("Stack ready")
print("Queue ready")
print("Linked list ready")
print("-"*20)

while True:
    print("1. Admin To Do List")
    print("2. Player Waiting List")
    print("3. Quest list")
    print ("4. Exit \n")
    ListChoice = int(input("Choose a list to modify: "))

    # Admin To Do List
    if ListChoice == 1:
        print("1. Add an admin action")
        print("2. Undo admin action")
        EditChoice = int(input("Choose an action: "))

    # Player Waiting List
    elif ListChoice ==2:
        print("1. Add a player")
        print("2. Remove a player")
        EditChoice = int(input("Choose an action: "))

    # Quest List
    elif ListChoice ==3:
        print("1. Add quest to complete")
        print("2. Finish/achieve a quest")
        print("3. Show current list of quests")
        EditChoice = int(input("Choose an action: "))

    else:
        exit()




