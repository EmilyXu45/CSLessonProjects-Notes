Stack = [None for i in range(10)] # Setting up a stack for 10 slots
BasePointer = 0 #0 because the list starts on index 0, this is the bottom of the stack, this should be constant
TopPointer = BasePointer - 1 # The stack is initially empty, when the first item is pushed in, the TopPointer will move from -1 to 0, which will point to the first item
StackFull = len(Stack)-1 # This indicates the last available position (NOT the size of the stack)

def push(item):
    global TopPointer, stackFull
    if TopPointer < stackFull: # The stack still has space; the last position has not been reached
        Stack[TopPointer + 1]= item # Add the data
        TopPointer += 1 # Update the pointer
        print (item, "pushed")
    else:
        print ("Stack is full, cannot push")
