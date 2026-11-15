from logging import StringTemplateStyle
from multiprocessing.connection import answer_challenge


class TreasureChest:
    # Private Attributes
    # __question: STRING
    # __answer: INTEGER
    # __points: INTEGER
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
        


