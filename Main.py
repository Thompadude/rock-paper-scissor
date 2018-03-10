from CalculateWinner import calculate_winner
from Shape import Shape

shape = 0
while shape < 1 or shape > 3:
    try:
        shape = int(input("Choose your shape.\n1. Rock\n2. Paper\n3. Scissor\nInput: "))
    except ValueError:
        print("Invalid choice")
    if shape < 3:
        print("Number too low")
    else:
        print("Number too high")

userShape = Shape.get_shape(shape)
aiShape = Shape.get_ai_choice()

print("Choice: ", userShape)
print("AI choice is", aiShape)

calculate_winner(userShape, aiShape)
