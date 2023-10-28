import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_game(rounds):
    player1_score = 0
    player2_score = 0

    for round_num in range(1, rounds + 1):
        input(f"Round {round_num}: Press Enter to roll the dice...")
        
        player1_roll = roll_dice()
        player2_roll = roll_dice()

        print(f"Player 1 rolled: {player1_roll}")
        print(f"Player 2 rolled: {player2_roll}")

        if player1_roll > player2_roll:
            print("Player 1 wins this round!")
            player1_score += 1
        elif player2_roll > player1_roll:
            print("Player 2 wins this round!")
            player2_score += 1
        else:
            print("It's a tie for this round!")

        print(f"Player 1 Score: {player1_score}")
        print(f"Player 2 Score: {player2_score}")
        print("")

    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds to play: "))
    play_dice_game(rounds)
