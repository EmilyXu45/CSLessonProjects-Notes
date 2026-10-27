'''
# Countdown function
def countdown(n):
    if n == -1:
        print("Blast off")
    else:
        print(n)
        countdown(n-1)
start = int(input("Enter a starting number: "))
countdown(start)

def factorial (n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial (4))

def fib(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

def gcd (a, b):
    if b==0:
        # After each pass, b becomes a and a%b becomes b
        return a
    else:
        return gcd(b, a%b)
print(gcd(48, 18))

def binary_search(list, first, last, to_find):
  if first > last:
    return -1
  middle = (first + last)//2

  if list[middle] == to_find:
    return middle
  if list[middle]> to_find:
    return binary_search(list, first, middle -1, to_find)
  else:
    return binary_search(list, middle+1, last, to_find)

list = [1,3,4,5,7]
to_find = int(input("Enter a number to find: "))
print(binary_search(list, 0, len(list)-1, to_find))


def hanoi(disks, start, helper, end):
    if disks == 1:
        print("Move disk from", start, "to", end)
    else:
        hanoi(disks-1, start, end, helper)
        print("Move disk from", start, "to", end)
        hanoi(disks-1, helper, start, end)
        pass

hanoi(3, "A", "B", "C")
print("Hanoi complete")


def gray(n):
    if n ==1:
        return['0','1']
    smaller = gray(n - 1)
    first_half= ["0"+code for code in smaller]
    second_half=["1"+code for code in smaller]
    return first_half+second_half
bits = int(input("Bits: "))
print(gray(bits))

'''
