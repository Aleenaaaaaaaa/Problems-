import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Game! 🎲")
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

play_again = "y"

while play_again.lower() == "y":
    input(f"\n{player1}, press Enter to roll the dice...")
    roll1 = roll_dice()
    print(f"{player1} rolled a {roll1}")

    input(f"\n{player2}, press Enter to roll the dice...")
    roll2 = roll_dice()
    print(f"{player2} rolled a {roll2}")

    if roll1 > roll2:
        print(f"\n🏆 {player1} wins this round!")
    elif roll2 > roll1:
        print(f"\n🏆 {player2} wins this round!")
    else:
        print("\nIt's a tie!")

    play_again = input("\nDo you want to play again? (y/n): ")

print("\nThanks for playing! 🎉")
