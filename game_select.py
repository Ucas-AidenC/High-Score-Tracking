import csv  # Import the CSV module to read leaderboard files

def display_leaderboard(filename, game_name):
    # Reads and displays the leaderboard for a given game. The format is: place - score - username.
    
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)  
        next(csv_reader)  # Skip the header row

        print(f"\n    {game_name}\n")  # Display the game name with spacing
        
        for row in csv_reader:
            print(f"{row[0]} - {row[1]} - {row[2]}")  # Print each leaderboard entry in the required format

def display_all_leaderboards():
    # Calls display_leaderboard for all available games to print all leaderboards.
    
    display_leaderboard("guessing_game.csv", "Guess the Number")  
    display_leaderboard("text_adventure.csv", "Adventure")  

def game_selector():
    # Provides a menu for the user to play a game, view leaderboards, or return to the main menu.

    while True:

        try:
            select = int(input("\nWhere would you like to go?\n(1) Play Guess the Number\n(2) Play Adventure\n(3) Display all leaderboards\n(4) Return to main menu\nPlease type the number corresponding to your selection: "))  # Convert input to an integer for validation

            if select == 1:
                display_leaderboard("guessing_game.csv", "Guess the Number")  # Show leaderboard before launching game
                
                try:
                    play_choice = int(input("\nWould you like to play this game?\n(1) Yes\n(2) No\nPlease type the number corresponding to your selection: "))
                    
                    if play_choice == 1:
                        # This is where the code for running the game will be inserted
                        print("\nLaunching Guess the Number...")  

                    elif play_choice == 2:
                        print("\nReturning to game selection menu...")  

                    else:
                        print("\nInvalid input. Please enter 1 or 2. Returning to the game selection menu...")  

                except ValueError:
                    print("\nInvalid input. Please enter a whole number from 1-2. Returning to the game selection menu...")  

            elif select == 2:
                display_leaderboard("text_adventure.csv", "Adventure")  # Show leaderboard before launching game
                
                try:
                    play_choice = int(input("\nWould you like to play this game?\n(1) Yes\n(2) No\nPlease type the number corresponding to your selection: "))
                    
                    if play_choice == 1:
                        # This is where the code for running the game will be inserted
                        print("\nLaunching Adventure...")  

                    elif play_choice == 2:
                        print("\nReturning to game selection menu...")  

                    else:
                        print("\nInvalid input. Please enter 1 or 2. Returning to the game selection menu...")  

                except ValueError:
                    print("\nInvalid input. Please enter a whole number from 1-2. Returning to the game selection menu...")  

            elif select == 3:
                display_all_leaderboards()  # Show all leaderboards

            elif select == 4:
                print("\nReturning to main menu...")  # Exit the menu
                break  

            else:
                print("\nInvalid selection. Please enter a number 1-4.")  # Handle invalid number selections

        except ValueError:
            print("\nInvalid input. Please enter a whole number.")  # Handle cases where user input is not a valid number

game_selector()  # Run the game selector menu
