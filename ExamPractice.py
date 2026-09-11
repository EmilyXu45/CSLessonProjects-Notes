# Declaring global variables and initialising pointers
queue = [-1 for i in range(11)]
headpointer = -1
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

for i in range (1,12):
    Enqueue(i)
print (queue)
