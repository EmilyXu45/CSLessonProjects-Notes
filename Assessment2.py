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
    lines = file.readlines()
for i in range(0, len(lines)-1, 2):
    topic = lines[i].strip()
    question = lines[i+1].strip()
    if topic not in topics_and_questions:
        topics_and_questions[topic] = []
    topics_and_questions[topic].append(question)

# (c) Unique list of topics
unique_topics = list(topics_and_questions.keys())

# (d) Choosing a topic + validation, printing a random question, outputting the time required
import random
UserTopic = input("Enter a topic to practice: ")
StartTime = input("Enter the start time HH:MM: ")
while UserTopic not in unique_topics:
    UserTopic = input("Topic invalid, enter again: ")
topicalquestions = topics_and_questions[UserTopic]
question = random.choice(topicalquestions)
print("Topic: ", UserTopic)
print("Question: ", topicalquestions)

parts = StartTime.split(":")
hours = int(StartTime[0])
mins = int(StartTime[1])
totalMins = mins + 40
additionalHour = totalMins//60
MinsPart = totalMins % 60
HoursPart = (hours + additionalHour) % 24
print(f"Finished Time: {HoursPart}:{MinsPart}")





