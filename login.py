import csv

profiles = []
profile_names = []

selected_profile = {}

def read_profiles():

    with open('profile_file.csv', 'r') as profile_file:

        csvFile = csv.reader(profile_file)

        for profile in csvFile:

            if profile[0] not in profile_names:
                profile_names.append(profile[0])

            if profile[0] != 'name' and profile[1] != 'password':
                profiles.append({'name': profile[0], 'password': profile[1]})

def append_profile(name,password):

    with open('profile_file.csv', 'a', newline='') as profile_file:

        profile_writer = csv.writer(profile_file)
        profile_writer.writerow([name,password])

def add_profile():
    input("No profile was found.")
    input("Creating new profile...")
            
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

                            password_guess = input('What is the profile password? (Type "Exit" to change profile)')

                            if password_guess == profile['password']:
                                return profile
                            
                            elif password_guess.lower() == 'exit':
                                break

        else:   
            add_profile()
            
selected_profile = login()

print(selected_profile)

def main():
    
    match input('What menu do you want to access? \n1. Games \n2. Profiles \n3. Exit'):
        
        case '2':

            match input('What do you want to do? \n1. Add Profile \n2. Remove Profile \n3. Change Profile'):

                case '1':
                    add_profile()
                
                case '3':
                    login()