import csv

profiles = []

def read_profiles():

    with open('profiles_file.csv', 'r') as csvfile:

        for line in csvfile:

            # Splits the csv file by line then by value type (name or password) 
            data = line.split(',')
            profile = {'name': '', 'password': ''}

            i = 0
            for value in data:

                # IF value is name
                if i % 2 == 0:
                    profile['name'] = value

                # IF value is password
                else:
                    profile['password'] = value
                    profiles.append(profile)

                i += 1

    profiles.pop(0)

def create_profile(name, password):

    with open('profiles_file.csv', 'a', newline='') as csvfile:

        fieldnames = ['name', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'name': name, 'password': password}])

def login_menu():

    read_profiles()

    profile_names = []

    for profile in profiles:
        profile_names.append(profile['name'])

    while True:

        # IF there is a profile in profiles
        if profiles:

            print('Profiles:')
            
            for profile_name in profile_names:
                print(f'- {profile_name}')

        else:

            input('No Profile Found.')
            input('Creating Profile...')
            create_profile(input('Choose a username: '), input('Choose a password: '))

import csv

profiles = [{'name': 'John_Doe', 'password': '12345'}]

def read_profiles():

    with open('profile_file.csv', 'r') as profile_file:
        csvFile = csv.reader(profile_file)
        for profile in csvFile:
            profiles.append(profile)

def write_profiles():

    with open('profile_file.csv', 'w', newline='') as profile_file:
        fieldnames = ['name', 'password']
        writer = csv.DictWriter(profile_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)

def create_profile():

    name = input('Choose a username for your profile: ')
    password = input('Choose a password for your profile: ')

    profiles.append({'name': name, 'password': password})

read_profiles()

for profile in profiles:
    print(f"{profile['name']}: {profile['password']}")

create_profile()
write_profiles()

for profile in profiles:
    print(f"{profile['name']}: {profile['password']}")
