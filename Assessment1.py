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
        print(card, "pushed")
    else:
        print("Stack is full, cannot push card")

def Pop():
    global TopPointer
    if TopPointer < BottomPointer:
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
    parts = Card.strip().split(",")
    rank = parts [0]
    suit = parts[1]
    print(rank, "of", suit)

