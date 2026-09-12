Stack = [None for i in range(10)] # Setting up a stack for 10 slots
BasePointer = 0 #0 because the list starts on index 0, this is the bottom of the stack, this should be constant
TopPointer = BasePointer - 1 # The stack is initially empty, when the first item is pushed in, the TopPointer will move from -1 to 0, which will point to the first item
StackFull = len(Stack)-1 # This indicates the last available position (NOT the size of the stack)

def push(item):
    global TopPointer, Stack
    if TopPointer < StackFull: # The stack still has space; the last position has not been reached
        Stack[TopPointer + 1]= item # Add the data
        TopPointer += 1 # Update the pointer
        print (item, "pushed")
    else:
        print ("Stack is full, cannot push")

def pop():
    global TopPointer, Stack
    if BasePointer <= TopPointer: # Check whether the stack contains at least 1 item, if the TopPointer is above the BasePointer then the stack is not empty
        item_removed = Stack[TopPointer] # Store the value that is going to be removed
        Stack[TopPointer] = None # Replace the value with an empty slot
        TopPointer -= 1 # Move the TopPointer so that it points to the previous value
        print(item_removed, "popped")
    else:
        print("Stack is empty, cannot pop")

for i in range (10):
    push(i)
pop()
pop()
print(Stack)