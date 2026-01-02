# Import the random module to generate random numbers
import random

# Initialize score to keep track of correct guesses
score = 0

# Display welcome message
print("Welcome to Number Guessing Game")

# Main game loop (runs until user decides to stop)
while True:

    # Step 1: Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Step 2: Set number of attempts
    attempts = 3

    print("\nI have selected a number between 1 and 10.")
    print("You have 3 attempts to guess it.")

    # Loop for guessing attempts
    while attempts > 0:
        try:
            # Step 3: Take user input
            guess = int(input("Enter your guess: "))
        except ValueError:
            # Step 4: Handle invalid (non-number) input
            print("Invalid input. Please enter a number.")
            continue

        # Step 5: Check if the guess is correct
        if guess == number:
            print("Correct! You guessed the number.")
            score += 1          # Increase score for correct guess
            break               # Exit attempt loop

        # Step 6: Give hint if guess is wrong
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        # Step 7: Reduce attempts after wrong guess
        attempts -= 1

    # Step 8: If all attempts are used
    if attempts == 0:
        print(f"You lost! The number was {number}")

    # Step 9: Display current score
    print(f"Current Score: {score}")

    # Step 10: Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    # Step 11: End the game if user says no
    if play_again != "yes":
        print("Thank you for playing.")
        break
