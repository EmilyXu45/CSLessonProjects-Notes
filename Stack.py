Stack = [None for i in range(10)] # Setting up a stack for 10 slots
BasePointer = 0 #0 because the list starts on index 0, this is the bottom of the stack, this should be constant
TopPointer = BasePointer - 1 # The stack is initially empty, when the first item is pushed in, the TopPointer will move from -1 to 0, which will point to the first item
StackFull = len(Stack)-1 # This indicates the last available position (NOT the size of the stack)

