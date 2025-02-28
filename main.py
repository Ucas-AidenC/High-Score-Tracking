import login
import game_select

def main():
    # Ensure the user logs in before anything else
    selected_profile = login.login()

    while True:
        print(f"Welcome {selected_profile['name']}")
        print("1. Games")
        print("2. Profiles")
        print("3. Exit")
        choice = input("Enter a number: ")

        if choice == "1":
            game_select.game_selector()  # Now properly called inside the loop

        elif choice == "2":
            while True:
                print(f"Welcome {selected_profile['name']}")
                print("1. Add Profile")
                print("2. Remove Profile")
                print("3. Change Profile")
                print("4. Back")
                profile_choice = input("Enter a number: ")

                if profile_choice == "1":
                    login.add_profile()
                elif profile_choice == "2":
                    selected_profile = login.remove_profile()
                elif profile_choice == "3":
                    selected_profile = login.login()
                elif profile_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
