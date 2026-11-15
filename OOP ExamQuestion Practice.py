import os

# Question 3
# part 3(a)
class TreasureChest:
    # DECLARE question: STRING
    # DECLARE answer: INTEGER
    # DECLARE points: INTEGER

    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    # part 3(c)(i)
    def getQuestion(self):
        return self.__question

    # part 3(c)(ii)
    def checkAnswer(self, answer):
        if answer == self.__answer:
            return True
        else:
            return False

    # part 3(c)(iii)
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points/2
        elif attempts == 3 or attempts == 4:
            return self.__points/4
        else:
            return 0

# part 3(b)
# DECLARE arrayTreasure: TreasureChest
arrayTreasure = []

def readData():
    try:
        with open("TreasureChestData.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(0, len(lines), 3):
                question = lines[i].strip()
                answer = int(lines[i + 1].strip())
                points = int(lines[i + 2].strip())

                Question = TreasureChest(question, answer, points)
                arrayTreasure.append(Question)
    except OSError:
        print("File is NOT found!")

# part 3(c)(iv)
readData()
choice = int(input("Choose a question between 1 to 5: "))
selectedQuestion = arrayTreasure[choice-1]
print(selectedQuestion.getQuestion())

Attempts = 0
Correct = False
while not Correct:
    UserAnswer = int(input("Enter your answer: "))
    if selectedQuestion.checkAnswer(UserAnswer) == True:
        Correct = True
    Attempts += 1
points = selectedQuestion.getPoints(Attempts)
print(points, "awarded to user!")

