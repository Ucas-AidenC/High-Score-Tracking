import scores  # This stays to ensure score updates
import TextAdventure
import guessing_game
import login  # Import login to get the username

# Code originally written by Mark

# Display the leaderboard from the dictionary
def display_leaderboard(game_file, game_name):
    scores.update_dictionary_from_csv(game_file)  # Ensure dictionary is up to date

    print(f"\n    {game_name} Leaderboard\n")  # Display the game name with spacing
    sorted_scores = sorted(scores.scores_dict.items(), key=lambda x: x[1], reverse=True)

    place = 1
    for username, score in sorted_scores[:10]:  # Limit to top 10
        print(f"{place} - {score} - {username}")
        place += 1

# Display all leaderboards
def display_all_leaderboards():
    display_leaderboard("guessing_game.csv", "Guess the Number")
    display_leaderboard("text_adventure.csv", "Adventure")

def game_selector():
    while True:
        try:
            select = int(input("\nWhere would you like to go?\n1. Play Guess the Number\n2. Play Adventure\n3. Display all leaderboards\n4. Return to main menu\nPlease type the number corresponding to your selection: "))

            # Number Game
            if select == 1:
                display_leaderboard("guessing_game.csv", "Guess the Number")
                play_choice = int(input("\nWould you like to play this game?\n1. Yes\n2. No\nPlease type the number corresponding to your selection: "))

                if play_choice == 1:
                    print("\nLaunching Guess the Number...")
                    score = guessing_game.play_game()
                    username = login.selected_profile['name']
                    scores.compare("guessing_game.csv", username, score)

            # Text Adventure
            elif select == 2:
                display_leaderboard("text_adventure.csv", "Adventure")
                play_choice = int(input("\nWould you like to play this game?\n1. Yes\n2. No\nPlease type the number corresponding to your selection: "))

                if play_choice == 1:
                    print("\nLaunching Adventure...")
                    TextAdventure.main()
                    username = login.selected_profile['name']
                    score = TextAdventure.player_stats['score']
                    scores.compare("text_adventure.csv", username, score)
                    print("\nYour score has been recorded!")

            # Display all leaderboards
            elif select == 3:
                display_all_leaderboards()

            # Return to main menu
            elif select == 4:
                print("\nReturning to main menu...")
                break
            
            # Invalid Input
            else:
                print("\nInvalid selection. Please enter a number 1-4.")

        except ValueError:
            print("\nInvalid input. Please enter a whole number.")

if __name__ == "__main__":
    game_selector()
