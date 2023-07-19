import random
moves = ['R', 'P', 's']
def display_results(player, computer):
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == 'R':
        if computer == 'P':
            print("P covers R. You lose.")
        if computer == 'S':
            print("R crushes S. You win!")
    elif player == 'P':
         if computer == 'R':
            print("P covers R. You win!")
         if computer == 'S':
            print("S cuts P. You lose.")
    elif player == 'S':
        if computer == 'R':
            print("R crushes S. You lose.")
        if computer == 'P':
            print("S cuts P. You win!")

computer = random.choice(moves)

player = input("Enter a choice (R, P, S): ")
while player not in moves:
    player = input("Invalid input. Enter a choice (R, P, S): ")

display_results(player, computer)

print(f"Computer played {computer}")
print(f"Player played {player}")