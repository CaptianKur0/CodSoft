import random
print("Welcome to Rock, Paper, Scissors Game!")

score = 0
system = 0
round_num = 1

while True:
    print()
    print("Round", round_num)
    print("Type rock, paper, or scissors.")
    user_input = input("Your choice: ")

    user_input = user_input.lower()

    if user_input != "rock" and user_input != "paper" and user_input != "scissors":
        print("Oops, that's not a valid choice. Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)

    if user_input == computer_choice:
        print("It's a tie!")
    elif user_input == "rock":
        if computer_choice == "scissors":
            print("You win this round!")
            score = score + 1
        else:
            print("You lose this round!")
            system = system + 1
    elif user_input == "paper":
        if computer_choice == "rock":
            print("You win this round!")
            score = score + 1
        else:
            print("You lose this round!")
            system = system + 1
    elif user_input == "scissors":
        if computer_choice == "paper":
            print("You win this round!")
            score = score + 1
        else:
            print("You lose this round!")
            system = system + 1

    print("Score: You =", score, "Computer =", system)

    play_again = input("Play again? (yes or no): ")
    play_again = play_again.lower()
    if play_again != "yes" and play_again != "y":
        print()
        print("Thanks for playing!")
        print("Final score: You =", score, "Computer =", system)
        break

    round_num = round_num + 1
