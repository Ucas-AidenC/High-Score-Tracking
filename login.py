import csv

profiles = []
profile_names = []

selected_profile = {'name': 'name', 'password': 'password'}

# Reads profile onto profiles
def read_profiles():

    with open('profile_file.csv', 'r') as profile_file:

        csvFile = csv.reader(profile_file)

        for profile in csvFile:
            
            # Cheacks if profile isn't the same as the header or if there already is a profile name
            if (profile[0] != 'name' and profile[1] != 'password') and (profile[0] not in profile_names):

                profiles.append({'name': profile[0], 'password': profile[1]})

            if profile[0] not in profile_names:
                profile_names.append(profile[0])

# Adds profile to file
def append_profile(name,password):

    with open('profile_file.csv', 'a', newline='') as profile_file:

        profile_writer = csv.writer(profile_file)
        profile_writer.writerow([name,password])

# Adds profile to profiles
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

# Removes a profile
def remove_profile():

    profile_to_delete = {}
    profile_selected = False

    while not profile_selected:

        for profile in profiles:
            print(f'- {profile['name']}')

        profile_name = input('What profile do you want to remove? (Enter "Exit" to back out) ')

        if profile_name.lower() == 'exit':
            return selected_profile
        
        # Checks if profile exists
        if profile_name in profile_names:

            for profile in profiles:
                
                # Has user input a password before deleting the profile
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

    read_profiles()

    # Reappends the header
    for profile in profiles:
        profiles_lists.append([profile['name'], profile['password']])
    
    # Readds profiles onto profile
    with open('profile_file.csv', 'w', newline='') as profile_file:

        profile_writer = csv.writer(profile_file)
        profile_writer.writerows(profiles_lists)

    # Has user relogin if they're deleting the profile they're on
    if profile_to_delete == selected_profile:
        read_profiles
        return login()
    else:
        read_profiles()
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