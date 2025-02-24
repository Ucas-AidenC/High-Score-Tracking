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
