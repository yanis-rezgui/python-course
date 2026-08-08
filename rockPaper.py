import random


def pickComputerMove():

    randomNumber = random.random()

    computerMove = ""

    if randomNumber < 1 / 3:
        computerMove = "rock"
    elif randomNumber < 2 / 3:
        computerMove = "paper"
    else:
        computerMove = "scissors"

    return computerMove


def play_round(player_move, computer_move):
    """Compare le coup du joueur et de l'ordinateur et renvoie le résultat."""
    # Cas 1 : Égalité
    if player_move == computer_move:
        return "Tie"

    # Cas 2 : Victoire du joueur
    elif (
        (player_move == "rock" and computer_move == "scissors")
        or (player_move == "paper" and computer_move == "rock")
        or (player_move == "scissors" and computer_move == "paper")
    ):
        return "You win"

    # Cas 3 : Dans tous les autres cas, c'est l'ordinateur qui gagne
    else:
        return "You lose"


def pickPlayerMove(playerMove):

    index = 0

    print("\n1 for rock:")
    print("\n2 for paper")
    print("\n3 for scissors")

    while index < 1 or index > 3:
        index = int(input("tape a number"))

    match index:
        case 1:
            playerMove = "rock"
        case 2:
            playerMove = "paper"
        case 3:
            playerMove = "scissors"

        case _:
            print("wrong number")

    return playerMove
