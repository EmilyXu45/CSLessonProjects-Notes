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
    with left_col:
        st.header("Binary Search")
        st.write("Splits a sorted list in half to quickly locate an item.")
        # ---> Add your explanation here

    with right_col:
        st.subheader("Visualization")
        # ---> Add your visualization code here

# 3. BUBBLE SORT
elif st.session_state.algo == "Bubble Sort":
    with left_col:
        st.header("Bubble Sort")
        st.write("Repeatedly swaps adjacent elements if they are out of order.")
        # ---> Add your explanation here

    with right_col:
        st.subheader("Visualization")
        # ---> Add your visualization code here

# 4. INSERTION SORT
elif st.session_state.algo == "Insertion Sort":
    with left_col:
        st.header("Insertion Sort")
        st.write("Builds the sorted array step-by-step by placing each item into position.")
        # ---> Add your explanation here

    with right_col:
        st.subheader("Visualization")
        # ---> Add your visualization code here