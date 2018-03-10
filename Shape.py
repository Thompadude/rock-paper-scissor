from random import randint


class Shape:
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSOR = "Scissor"

    @staticmethod
    def get_shape(number):
        if number == 1:
            return Shape.ROCK
        elif number == 2:
            return Shape.PAPER
        return Shape.SCISSOR

    @staticmethod
    def get_ai_choice():
        return Shape.get_shape(randint(1, 3))
