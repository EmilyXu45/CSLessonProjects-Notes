# Tutorial: https://jamesabela.github.io/jsfun/sorts_searches_course/12_final_project.html
# Breadcrumb: Level 12 of 12 - Sorts and Searches

print("Algorithm Arcade")
print("Your task:")
print("1. Add at least two algorithms")
print("2. Count comparisons")
print("3. Explain worst-case Big O")
print("4. Add a turtle visualisation if you can")

# Build your project below.

import streamlit as st
import time

st.set_page_config(page_title="Algorithm Revision", layout="wide")


if "algo" not in st.session_state:
    st.session_state.algo = "Linear Search"

st.title("Algorithm Revision App")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Linear Search", use_container_width=True):
        st.session_state.algo = "Linear Search"
with col2:
    if st.button("Binary Search", use_container_width=True):
        st.session_state.algo = "Binary Search"
with col3:
    if st.button("Bubble Sort", use_container_width=True):
        st.session_state.algo = "Bubble Sort"
with col4:
    if st.button("Insertion Sort", use_container_width=True):
        st.session_state.algo = "Insertion Sort"

st.divider()

left_col, right_col = st.columns([1, 1])

if st.session_state.algo == "Linear Search":
    st.header("Linear Search")
    st.write("Checks each element in a list from the start until it finds the target value or reaches the end of the list.")
    
    st.subheader("Sample Code")
    st.code("""
numbers = [4, 8, 15, 16, 23, 42]
target = int(input("Target: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        print("Found at index", i)

if found == False:
    print("Not found")

""", language="python")

    st.write("**Time Complexity:** $O(n)$")
    st.header("Explanation")
    st.write("""  1. Linear search works on both sorted and unsorted lists. \n
    2. It is inefficient for large lists because it checks every element one by one, sequentially. \n
    3. The time O(n) means that the time taken to search for an element grows linearly in proportion to n (the number of elements in the list) \n
    4. In the worst case, the target value is missing or located last, so algorithm must check all n elements. """)

    
# 2. BINARY SEARCH
elif st.session_state.algo == "Binary Search":
    st.write("Checks the middle element of a sorted list and eliminates half the search space with each comparison.")
    
    st.subheader("Sample Code")
    st.code("""
numbers = [2, 5, 7, 9, 12, 15, 19]
low = 0
high = len(numbers) - 1
middle = (high + low) // 2
print("Middle index", middle)
print("Middle value", numbers[middle])

numbers = [2, 5, 7, 9, 12, 15, 19, 22, 31]
target = int(input("Target: "))
low = 0
high = len(numbers) - 1
found = False

while low <= high and found == False:
    middle = (low + high) // 2
    if numbers[middle] == target:
        found = True
        print("Found at index", middle)
    elif target < numbers[middle]:
        high = middle - 1
    else:
        low = middle + 1

if found == False:
    print("Not found")

""", language="python")

    st.write("**Time Complexity:** $O(Log (n))$")
    st.header("Explanation")
    st.write("""  1. Binary search works only on sorted lists. \n
    2. It is efficient for large lists because it eliminates half the search space with each comparison. \n
    3. The time O(Log n) means that the time taken to search for an element grows logarithmically in proportion to n (the number of elements in the list) \n
    4. In the worst case, the target value is missing or located at one of the ends, so algorithm must check Log n elements. """)

# 3. BUBBLE SORT
elif st.session_state.algo == "Bubble Sort":
    st.write("Repeatedly swaps adjacent elements if they are out of order.")
    
    st.subheader("Sample Code")
    st.code("""
numbers = [9, 4, 7, 1]

for pass_num in range(len(numbers)):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp

print(numbers)

""", language="python")

    st.write("**Time Complexity:** $O(N^2)$")
    st.header("Explanation")
    st.write("""  1. Bubble sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. \n
    2. The pass through the list is repeated until the list is sorted. \n
    3. The time $n^2$ means that the time taken to sort the list grows quadratically in proportion to n (the number of elements in the list) \n
    4. In the worst case, the target value is missing or located at one of the ends, so algorithm must check $n^2$ elements. """)

# 4. INSERTION SORT
elif st.session_state.algo == "Insertion Sort":
    st.write("Builds the sorted array step-by-step by placing each item into position.")
    
    st.subheader("Sample Code")
    st.code("""
numbers = [6, 3, 8, 2]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = key

print(numbers)

""", language="python")

    st.write("**Time Complexity:** $O(N^2)$")
    st.header("Explanation")
    st.write("""  1. Insertion sort builds the sorted array step-by-step by placing each item into position. \n
    2. It is efficient for small lists and lists that are already mostly sorted. \n
    3. The time $n^2$ means that the time taken to sort the list grows quadratically in proportion to n (the number of elements in the list) \n
    4. In the worst case, the target value is missing or located at one of the ends, so algorithm must check $n^2$ elements. """)