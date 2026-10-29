# Question 1
# (a) Creating a recursive_sum function
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return recursive_sum(n-1)+n
print(recursive_sum(3))

# (b) Dictionary for first 10 recursive sums
Sums = {}
for i in range(1,11):
    # Assigning the value (recursive_sum(i)) to the key i
    Sums[i] = recursive_sum(i)
print(Sums)

# Mistake correction: this creates a set; dictionaries must use colon, sets are unordered which means that the numbers are arranged based on internal memory hashes rather than the order
# Difference between set & dictionaries: A set is a collection of unique values while a dictionary is collection of key value pairs.
'''
sums = {}
for i in range(1,11):
    sums = {i, recursive_sum(i)}
    print(sums)
'''

# Question 2
# (a) Creating a suitable data structure to store the topics and the question
topics_and_questions = {}

# (b) Extracting all the topics and questions
with open("ielts.txt", "r") as file:
    # Reading all the lines in the file into a list
    lines = file.readlines()
# Loop through all the lines in steps of 2, even index: topic, odd index: question (start on 0)
for i in range(0, len(lines)-1, 2):
    # Extract the topic and question, strip the blank line
    topic = lines[i].strip()
    question = lines[i+1].strip()
    # If a topic (key) appears for the first time, the value can't be added to a non-existent key, so the key(topic) needs to be created first before the value can be appended to it
    if topic not in topics_and_questions:
        topics_and_questions[topic] = []
    # Adding the question (value) to the dictionary
    topics_and_questions[topic].append(question)

# (c) Unique list of topics: keys() will only get the topic (key) once even if it has been repeated in the dictionary
unique_topics = list(topics_and_questions.keys())

# (d) Choosing a topic + validation, printing a random question, outputting the time required
import random
UserTopic = input("Enter a topic to practice: ")
StartTime = input("Enter the start time HH:MM: ")
# Validating user's input
while UserTopic not in unique_topics:
    UserTopic = input("Topic invalid, enter again: ")
# Creating a list of questions based on the same key
topicalquestions = topics_and_questions[UserTopic]
# Choosing a random question from the list of topical questions
question = random.choice(topicalquestions)
print("Topic: ", UserTopic)
print("Question: ", topicalquestions)

# Time entered needs to be a string so that it can be split into the hours and minutes parts
parts = StartTime.split(":")
# Convert each part back to integers so that we can calculate and convert the time accordingly
hours = int(StartTime[0])
mins = int(StartTime[1])
totalMins = mins + 40
# Finds any extra hours, if adding 40 mins will change the hour
additionalHour = totalMins//60
# Finds remainder after the (additional) hour part has been extracted
MinsPart = totalMins % 60
# Finds & resets the hours part if it passes over two days
HoursPart = (hours + additionalHour) % 24
print(f"Finished Time: {HoursPart}:{MinsPart}")





