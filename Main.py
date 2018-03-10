from CalculateWinner import calculate_winner
from Shape import Shape

shape = 0
while shape < 1 or shape > 3:
    try:
        shape = int(input("Type a number and click enter.\n1 Rock\n2 Paper\n3 Scissor\nInput: "))
        if shape < 0:
            print("Number too low")
        elif shape > 3:
            print("Number too high")
    except ValueError:
        print("Invalid choice")

userShape = Shape.get_shape(shape)
aiShape = Shape.get_ai_choice()

print("Choice: ", userShape)
print("AI choice is", aiShape)

calculate_winner(userShape, aiShape)
