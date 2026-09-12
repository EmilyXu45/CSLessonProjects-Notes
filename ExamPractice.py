# Declaring global variables and initialising pointers
queue = [-1 for i in range(11)]
headpointer = 0
tailpointer = -1
queuelength = 0
queuefull = len(queue)

def Enqueue(item):
    global headpointer, tailpointer, queuelength, queuefull
    if queuelength<queuefull:
        tailpointer = tailpointer +1
        queue[tailpointer] = item
        queuelength = queuelength +1
        return True
    else:
        return False

def Dequeue ():
    global queue, headpointer, tailpointer, queuelength, queuefull
    if queuelength != 0:
        removed = queue[headpointer]
        queuelength -= 1
        queue[headpointer] = None
        if headpointer == queuefull -1:
            headpointer = 0
        else:
            headpointer += 1

        return removed
    else:
        return -1

for i in range(6):
    item = int(input("Enter integer: "))
    Enqueue(item)
for i in range (4):
    removed = Dequeue()
    print (removed)

