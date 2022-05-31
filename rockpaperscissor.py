import random


def play():
    user = input(
        "Please choose: \n(r) for rock, (p) for paper, (s) for scissor\nYour choice: ")
    computer = random.choice(["r", "p", "s"])

    print(f"The computer chooses {computer}")
    if user == computer:
        return "It is a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # return True if player wins

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        return True


print(play())
