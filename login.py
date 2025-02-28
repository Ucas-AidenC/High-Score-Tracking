import csv

profiles = []
profile_names = []

selected_profile = {'name': 'name', 'password': 'password'}

def read_profiles():

    with open('profile_file.csv', 'r') as profile_file:

        csvFile = csv.reader(profile_file)

        for profile in csvFile:

            if (profile[0] != 'name' and profile[1] != 'password') and (profile[0] not in profile_names):

                profiles.append({'name': profile[0], 'password': profile[1]})

            if profile[0] not in profile_names:
                profile_names.append(profile[0])

def append_profile(name,password):

    with open('profile_file.csv', 'a', newline='') as profile_file:

        profile_writer = csv.writer(profile_file)
        profile_writer.writerow([name,password])

def add_profile():
    
    input("Creating new profile... (Press Enter to continue)")
            
    while True:

        username, password = input('Choose a profile username: '), input('Choose a profile password: ')

        # Prevents user from making a profile that is the same as the header
        if username == 'name' and password == 'password':
            input('Invalid Username and Password. ')
            continue
                
        # Prevents the user from creating profiles with the same name
        redundent_name = False

        for profile_name in profile_names:
                    
            if username == profile_name:
                redundent_name = True
                
        if redundent_name == True:
            input('A profile already has that username. ')
            continue

        print(f'Username: {username} \nPassword: {password}')

        if input('Is this correct? If not, type "No": ').lower() == 'no':
            continue
        else:
            append_profile(username, password)
            read_profiles()
            break

def remove_profile():

    profile_to_delete = {}
    profile_selected = False

    while not profile_selected:

        for profile in profiles:
            print(f'- {profile['name']}')

        profile_name = input('What profile do you want to remove? (Enter "Exit" to back out) ')

        if profile_name.lower() == 'exit':
            return selected_profile
        
        if profile_name in profile_names:

            for profile in profiles:

                if profile_name == profile['name']:
        
                       while True:

                            password_guess = input('What is the profile password? (Type "Exit" to change profile) ')

                            if password_guess == profile['password']:
                                profile_to_delete = profile
                                profile_selected = True
                                break
                            
                            elif password_guess.lower() == 'exit':
                                break
        else:
            input('Could not find profile.')

    profiles.remove(profile_to_delete)

    profiles_lists = [['name', 'password']]

    for profile in profiles:
        profiles_lists.append([profile['name'], profile['password']])

    with open('profile_file.csv', 'w', newline='') as profile_file:

        profile_writer = csv.writer(profile_file)
        profile_writer.writerows(profiles_lists)

    if profile_to_delete == selected_profile:
        return login()
    else:
        return selected_profile


def login():
    
    read_profiles()

    while True:
        
        # IF there is a profile in profiles
        if profiles:

            for profile in profiles:
                print(f'- {profile['name']}')

            selected_profile_name = input('Choose a profile: ')
            if selected_profile_name in profile_names:

                for profile in profiles:

                    if selected_profile_name == profile['name']:
                        
                        while True:

                            password_guess = input('What is the profile password? (Type "Exit" to change profile) ')

                            if password_guess == profile['password']:
                                selected_profile['name'] = profile['name']
                                selected_profile['password'] = profile['password']
                                return selected_profile
                            
                            elif password_guess.lower() == 'exit':
                                break

        else:   
            input("No profile was found. (Press enter to continue)")
            add_profile()