import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Display results and update scores
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        # Display current score
        print(f"Score: You {user_score} - Computer {computer_score}")
        
        # Ask if user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final Score: You {user_score} - Computer {computer_score}")
    print("Thanks for playing!")

# Start the game
play_game()