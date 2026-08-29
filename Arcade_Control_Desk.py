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

def process_complete():
    print("-" * 20)
    print("Process complete")
    print("-" * 20)

# Lists to be used
AdminList = [
    "Add new arcade game",
    "Change game difficulty",
    "Update prize settings"
]

PlayerList = [
    "Alice",
    "Bob",
    "Carl"
]

# Menu
while True:
    print()
    print("1. Admin To Do List")
    print("2. Player Waiting List")
    print("3. Quest list")
    print ("4. Exit \n")
    ListChoice = int(input("Choose a list to modify: "))
    print("-" * 20)

    # Admin To Do List
    if ListChoice == 1:
        print("1. Add an admin action")
        print("2. Undo admin action\n")
        EditChoice = int(input("Choose an action: "))
        print("-" * 20)

        def AddAction(action):
            AdminList.append(action)
            print("-" * 20)
        def RemoveAction():
            AdminList.pop()
            print("-" * 20)

        print("Admin's Current To Do List:")
        for i in range(len(AdminList)):
            print (AdminList[i])
        if EditChoice == 1:
            print()
            action = input("Action to add: ")
            AddAction(action)
        else:
            RemoveAction()
        print("Admin's Updated To Do List")
        for i in range(len(AdminList)):
            print (AdminList[i])
        process_complete()


    # Player Waiting List
    elif ListChoice ==2:
        print("1. Add a player")
        print("2. Remove a player")
        EditChoice = int(input("Choose an action: "))
        print("-" * 20)

        def AddPlayer(player):
            PlayerList.append(player)
            print("-" * 20)
        def RemovePlayer():
            PlayerList.pop(0)
            print("-" * 20)

        print("Current Player Waiting List:")
        for i in range(len(PlayerList)):
            print (PlayerList[i])
        if EditChoice == 1:
            print()
            action = input("Player to add: ")
            AddPlayer(action)
        else:
            RemovePlayer()
        print("Updated Player Waiting List")
        for i in range(len(PlayerList)):
            print (PlayerList[i])
        process_complete()

    # Quest List
    elif ListChoice ==3:
        print("1. Add quest to complete")
        print("2. Finish/achieve a quest")
        print("3. Show current list of quests")
        EditChoice = int(input("Choose an action: "))



    else:
        exit()




