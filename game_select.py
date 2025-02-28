import csv  # Import the CSV module to read leaderboard files
import TextAdventure
import login  # Import login to get the username
import scores  # Import scores for score handling

def display_leaderboard(filename, game_name):
    # Reads and displays the leaderboard for a given game. The format is: place - score - username.
    
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)  
        next(csv_reader)  # Skip the header row

        print(f"\n    {game_name} Leaderboard\n")  # Display the game name with spacing
        
        for row in csv_reader:
            print(f"{row[0]} - {row[1]} - {row[2]}")  # Print each leaderboard entry in the required format

def display_all_leaderboards():
    # Calls display_leaderboard for all available games to print all leaderboards.
    
    display_leaderboard("guessing_game.csv", "Guess the Number")  
    display_leaderboard("text_adventure.csv", "Adventure")  