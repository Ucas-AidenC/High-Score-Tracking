#main.py initial commit
import login

selected_profile = {}

selected_profile = login.login()

def main():

    while True:

        match input(f'Welcome {selected_profile['name']} \nWhich menu do you want to access? \n1. Games \n2. Profiles \n3. Exit \nEnter a number: '):

            case '1':
                pass

            case '2':
                login.main()

            case '3':
                break

main()