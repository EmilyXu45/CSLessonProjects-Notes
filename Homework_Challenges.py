import random

DadJokes =[]

class Jokes:
    def __init__(self, prompt, answer):
        # DECLARE Prompt: STRING
        # DECLARE Answer: STRING
        self.__Prompt = prompt
        self.__Answer = answer

    def getJoke(self):
        return(self.__Prompt)

    def getAnswer(self):
        return(self.__Answer)


    def constructor(self):
        with open("DadJokes.txt","r") as file:
          lines= file.read().splitlines()
          for i in range (0, len(lines)-1, 2):
              question = lines[i].strip()
              answer = lines[i+1].strip()

              joke = Jokes(question, answer)
              DadJokes.append(joke)


    def printRandomJoke(self):
        chosen = random.randint(0, len(DadJokes) - 1)
        selectedjoke = DadJokes[chosen]
        print(selectedjoke.getJoke())
        UserAnswer = input("Enter your answer: ")
        if UserAnswer == selectedjoke.getAnswer():
            print("You are correct!")
        else:
            print(selectedjoke.getAnswer())

j = Jokes("", "")
j.constructor()
j.printRandomJoke()

import turtle

class pattern:
    # DECLARE __angle: INTEGER
    # DECLARE __times: INTEGER
    def __init__(self, angle, times):
        self.__angle = angle
        self.__times = times

    def draw_pattern(self):
        t = turtle.Turtle()
        t.speed(0)
        for i in range(self.__times):
            t.forward(100)
            t.right(self.__angle)

def get_patterns():
        with open("patterns.txt", "r") as file:
            lines = file.read().splitlines()
            for i in range(0, len(lines) - 1, 2):
                try:
                    angle = int(lines[i])
                    times = int(lines[i + 1])
                    pat = pattern(angle, times)
                    pat.draw_pattern()
                except ValueError:
                    continue

get_patterns()
turtle.done()

