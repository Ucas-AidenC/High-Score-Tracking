import random
import time

# Code originally by Aaron, rewritten by Mark

def time_delay():
    print("loading.")
    time.sleep(0.3)
    print("loading..")
    time.sleep(0.3)
    print("loading...")  
    time.sleep(0.5)

# Number guessing game
def play_game():
    attempts = 10  # Number of attempts per round
    total_score = 0  # Player's score
    rounds_left = 10  # Number of rounds

    print(" Welcome to the Number Guessing Game!\n")

    while rounds_left > 0:
        stop_game = input("If you want to exit the game, enter S, or enter anything to continue: ").capitalize()
        if stop_game == "S":
            print("Goodbye")
            break
        
        rounds_left -= 1
        number = random.randint(1, 50)  # Random number to guess
        time_delay()
        print(" Number is ready! Try to guess it.")

        total_score += guess_number(number, attempts)

    print(f"\n Game Over! Your final score: {total_score}")
    return total_score  # Return score instead of saving to a file

# Guessing function
def guess_number(number, attempts):
    print(f" The number is between 1 and 50. You have {attempts} tries!\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f" Attempt {attempt}:\t Your guess?: "))
        except ValueError:
            print(" Invalid input! Please enter a number!")
            continue

        if guess == number:
            print(f" Correct! The number was {number}.")
            return attempts - attempt + 1  # Higher score for fewer attempts

        print(" Wrong guess!", "Too high!" if guess > number else " Too low!")
        
        if abs(number - guess) <= 5:
            print(" Very close!")
        elif abs(number - guess) <= 10:
            print(" Closer!")

    print(f" Out of attempts! The number was {number}!")
    return 0  # No points if all attempts are used

# Start the game
if __name__ == "__main__":
    print("Welcome to the number guessing game!")
    play_game()
