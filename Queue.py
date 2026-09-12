# For a queue, index 0 is the front of the queue, and index 9 is the end of the queue
# For a stack, index 0 is the bottom of the stack, and index 9 is the top of the stack

Queue = [None for i in range(10)] # Setting up a queue of 10 slots
RearPointer = -1 # Points to the position of the last item in the queue (the one at the end of the queue)
FrontPointer = 0 # Points to the position of the first item in the queue (the one to be removed(
QueueFull = len(Queue) # Not using RearPointer -1 to indicate the size of the queue, because in a circular queue, the RearPointer can loop back, whereas in stack, this is not a problem.
QueueLength = 0 # Used to keep track of items in the queue

def enqueue(item):
    global RearPointer, FrontPointer, QueueLength, Queue, QueueFull
    # Move the pointers first
    if QueueLength < QueueFull: # if there are still space in the queue
        if RearPointer > QueueFull: # When RearPointer = QueueFull, the pointer must be at the end of the queue, but since there still spaces, this means that a circular queue must be implemented to loop back to the start.
            RearPointer = 0 # Looping back
        else:
            RearPointer += 1 # when the end is not reached, the pointer can just move to the next position.
        # Update the queue length
        QueueLength += 1
        # Enqueue the item
        Queue[RearPointer] = item
        print (item, "was enqueued")
    else:
        print("Queue is full, cannot enqueue")

def dequeue():
    global RearPointer, FrontPointer, QueueLength, Queue, QueueLength

    if QueueLength != 0: # Queue is not empty
        # Remove the data
        item_removed = Queue[FrontPointer] # Save the item that was removed
        Queue[FrontPointer] = None # Free up that slot
        QueueLength -= 1  # Decrease the queue size
        print(item_removed, "was dequeued")

        # Update the pointer to the position of the next data to be removed
        if FrontPointer == QueueFull - 1: # If the current removed data was at the last position of the queue, then the next data to be removed must be at the start of the queue (at index 0) because a circular queue is implemented.
            FrontPointer = 0
        else: # if the end of the queue is not reached, move onto the next position
            FrontPointer += 1
    else:
        print("Queue is empty, cannot dequeue")

for i in range (10):
    enqueue(i)
dequeue()
dequeue()
print(Queue)