import login
import game_select
import TextAdventure
import guessing_game
import scores

def main():
    # Ensure the user logs in before anything else
    selected_profile = login.login()

    while True:
        print(f"Welcome {selected_profile['name']}")
        print("1. Games")
        print("2. Profiles")
        print("3. Exit")
        choice = input("Enter a number: ")

        # Game selector
        if choice == "1":
            while True:

                try:
                    select = int(input("\nWhere would you like to go?\n(1) Play Guess the Number\n(2) Play Adventure\n(3) Display all leaderboards\n(4) Return to main menu\nPlease type the number corresponding to your selection: "))  # Convert input to an integer for validation

                    # Guess the Number Game
                    if select == 1:

                        game_select.display_leaderboard("guessing_game.csv", "Guess the Number")  # Show leaderboard before launching game
                        while True:
                        
                            try:
                                play_choice = int(input("\nWould you like to play this game?\n(1) Yes\n(2) No\nPlease type the number corresponding to your selection: "))

                                if play_choice == 1:
                                    # This is where the code for running the game will be inserted
                                    print("\nLaunching Guess the Number...")
                                    guessing_game.play_game()
                                    break

                                elif play_choice == 2:
                                    print("\nReturning to game selection menu...")
                                    break

                                else:
                                    print("\nInvalid input. Please enter 1 or 2.")  

                            except ValueError:
                                print("\nInvalid input. Please enter a whole number from 1-2.")  

                    elif select == 2:
                        game_select.display_leaderboard("text_adventure.csv", "Adventure")  # Show leaderboard before launching game
                        while True:
                            try:
                                play_choice = int(input("\nWould you like to play this game?\n(1) Yes\n(2) No\nPlease type the number corresponding to your selection: "))

                                if play_choice == 1:

                                    print("\nLaunching Adventure...")
                                    TextAdventure.main()
                                    username = login.selected_profile['name']
                                    score = TextAdventure.player_stats['score']
                        
                                    # Update leaderboard using scores.py logic
                                    scores.compare("text_adventure.csv", username, score)
                                    scores.save_to_profile(username, "user_profiles_text_adventure.csv", score)
                                    print("\nYour score has been recorded!")
                                    break

                                elif play_choice == 2:
                                    print("\nReturning to game selection menu...")
                                    break

                                else:
                                    print("\nInvalid input. Please enter 1 or 2.")  

                            except ValueError:
                                print("\nInvalid input. Please enter a whole number from 1-2.")  

                    elif select == 3:
                        game_select.display_all_leaderboards()  # Show all leaderboards

                    elif select == 4:
                        print("\nReturning to main menu...")  # Exit the menu
                        break  

                    else:
                        print("\nInvalid selection. Please enter a number 1-4.")  # Handle invalid number selections

                except ValueError:
                    print("\nInvalid input. Please enter a whole number.")  # Handle cases where user input is not a valid number

        elif choice == "2":
            while True:
                print(f"Welcome {selected_profile['name']}")
                print("1. Add Profile")
                print("2. Remove Profile")
                print("3. Change Profile")
                print("4. Back")
                profile_choice = input("Enter a number: ")

                # Add Profile
                if profile_choice == "1":
                    login.add_profile()

                # Remove Profile
                elif profile_choice == "2":
                    selected_profile = login.remove_profile()

                # Change Profile
                elif profile_choice == "3":
                    selected_profile = login.login()

                # Change Profile
                elif profile_choice == "4":
                    break

                # Invalid Input
                else:
                    print("Invalid choice. Please try again.")

        # Exit
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
