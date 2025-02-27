import login

selected_profile = {}

selected_profile = login.login()

def main(selected_profile):

    while True:

        match input(f'Welcome {selected_profile['name']} \nWhich menu do you want to access? \n1. Games \n2. Profiles \n3. Exit \nEnter a number: '):

            case '1':
                pass

            case '2':
                while True:

                    match input(f'Welcome {selected_profile['name']} \nWhat do you want to do? \n1. Add Profile \n2. Remove Profile \n3. Change Profile \n4. Back \nEnter a number: '):

                        case '1':
                            login.add_profile()

                        case '2':
                            selected_profile = login.remove_profile()
                
                        case '3':
                            selected_profile = login.login()

                        case '4':
                            break

            case '3':
                break

main(selected_profile)