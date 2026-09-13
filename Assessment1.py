# Task a - Create the stack:

stack = [None for i in range(52)]
BottomPointer = 0
TopPointer = BottomPointer -1
stackFull = len(stack) -1

def Push(card):
    global TopPointer
    if TopPointer < stackFull:
        TopPointer += 1
        stack[TopPointer] = card
    else:
        print("Stack is full, cannot push card")

def Pop():
    global TopPointer
    if TopPointer >= BottomPointer:
        removed = stack[TopPointer]
        stack[TopPointer] = None
        TopPointer -= 1
        return removed
    else:
        print("Stack is empty, cannot pop")

# Task b - Load the cards:

def LoadCards():
    with open("cards_with_values.txt", "r") as file:
        next(file)
        for card in file:
            parts = card.strip().split(",")
            rank = parts [0]
            suit = parts [1]
            value = parts [2]
            Card =str(rank) +" " + str(suit) +" " + value
            Push(Card)
            value = int(parts [2]) # Update value so that it is an integer

# Task c - Display a card

def DisplayCard(Card):
    parts = Card.strip().split(" ")
    rank = parts [0]
    suit = parts[1]
    print(rank, "of", suit)

# Task d - Play the game

def PlayGame():
    LoadCards()
    score = 0

    if TopPointer < BottomPointer:
        return "No cards available to play."

    Card1 = Pop()

    while TopPointer >= BottomPointer:
        DisplayCard(Card1)
        Card1Value = int(Card1.split(" ")[2]) #Taking the value part

        choice = input("Will the next card be higher or lower? (H/L) or enter 'Q' to quit: ").upper()

        if choice == 'Q':
            break
        elif choice not in ['H', 'L']:
            print("Invalid input. Please enter H, L, or Q.")
            continue

        Card2 = Pop()
        DisplayCard(Card2)
        Card2Value = int(Card2.split(" ")[2])

        if Card2 > Card1 and choice == 'H':
            print("Correct!")
            score +=1
        elif Card2 < Card1 and choice == 'L':
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        Card1 = Card2

    print("Game Over! Final Score: ", score)

# Task e - Save the game

def SaveGame(score, current_card):
    with open("savegame.txt", "w") as file:
        file.write(str(score) + "\n")
        file.write(current_card + "\n")
        for i in range(BottomPointer, TopPointer + 1):
            file.write(stack[i] + "\n")

# Task f - Load a saved game
def LoadSavedGame():
    global TopPointer
    TopPointer = BottomPointer - 1

    with open("savegame.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()] # Read and remove white space for every line
        score = int(lines[0])
        Card1 = lines[1]
        for cards in lines[2:]:
            Push(cards)
    return score, Card1



