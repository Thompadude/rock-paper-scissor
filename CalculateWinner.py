from Shape import Shape


def calculate_winner(user_shape, ai_shape):
    if user_shape == ai_shape:
        print("Is it a draw")
    elif user_shape == Shape.ROCK and ai_shape == Shape.PAPER:
        print("You lost")
    elif user_shape == Shape.PAPER and ai_shape == Shape.SCISSOR:
        print("You lost")
    elif user_shape == Shape.SCISSOR and ai_shape == Shape.ROCK:
        print("You lost")
    else:
        print("You won!")
