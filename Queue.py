# For a queue, index 0 is the front of the queue, and index 9 is the end of the queue
# For a stack, index 0 is the bottom of the stack, and index 9 is the top of the stack

Queue = [None for i in range(10)] # Setting up a queue of 10 slots
RearPointer = -1 # Points to the position of the last item in the queue (the one at the end of the queue)
FrontPointer = 0 # Points to the position of the first item in the queue (the one to be removed(
QueueFull = len(Queue) # Not using RearPointer -1 to indicate the size of the queue, because in a circular queue, the RearPointer can loop back, whereas in stack, this is not a problem.
QueueLength = 0 # Used to keep track of items in the queue


