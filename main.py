import login
import game_select

# Code originally written by Darius, edited by Mark

def main():
    # Ensure the user logs in before anything else
    selected_profile = login.login()

    while True:
        print(f"Welcome {selected_profile['name']}")
        print("1. Games")
        print("2. Profiles")
        print("3. Exit")
        choice = input("Enter a number: ")

        # Games
        if choice == "1":
            game_select.game_selector()  # Now properly called inside the loop

        # Profiles
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

                # Back
                elif profile_choice == "4":
                    break

                # Invalid Input
                else:
                    print("Invalid choice. Please try again.")

        # Exit
        elif choice == "3":
            print("Exiting program.")
            break

        # Invalid Input
        else:
            print("Invalid choice. Please try again.")

main()

