#main.py initial commit
#ignore this
"""
r= Read(will give error if no file exists)
W=write (will give error if no file exists) 
W+= read and write (will give error if no file exists) 
A = append(add thing that cannot be overwritten)(will create a file if one doesn’t exist) 
A+ = read and append 
X = create a file 


import csv

# File paths
leaderboard_number = "leaderboard_number_guessing.csv"
leaderboard_adventure = "leaderboard_text_adventure.csv"
user_profile_number = "user_profiles_number_guessing.csv"
user_profile_adventure = "user_profiles_text_adventure.csv"

#dict storage 
scores = {}

# Loading scores 
def load_high_scores(game_file):
    with open(game_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                scores[row[0]] = int(row[1])
    return scores

#save scores to the csv 
def save_high_scores(game_file, scores):
    with open(game_file, "w", newline="") as file:
        writer = csv.writer(file)
        for user, score in scores.items():
            writer.writerow([user, score])

#saving to profile 
def save_to_profile(username, profile_file, score):
    with open(profile_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

#compare scores and update 
def compare(game_file, username, score):
    scores = load_high_scores(game_file)
    if username in scores:
        if score > scores[username]: 
            scores[username] = score
    else:
        scores[username] = score
    save_high_scores(game_file, scores)

#print for test
def print_leaderboard(game_file, game_name):
    scores = load_high_scores(game_file)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(game_name)
    for user, score in sorted_scores:
        print(f"{user}: {score}")

# print scores based on game 
def print_user_scores(username, profile_file, game_name):
    with open(profile_file, "r") as file:
        reader = csv.reader(file)
        print(username, game_name)
        for row in reader:
            if row[0] == username:
                print(f"{row[1]}")


#lil test function 
def main():
    while True:
        print("pick:")
        print("(1) Enter score")
        print("(2) Print leaderboard")
        print("(3). Print user scores")
        print("(4) Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            username = input("Enter your username: ")
            print("Select game")
            print("1. Number guessing game")
            print("2. Text adventure game")
            game_choice = input("Enter your choice (1-2): ")
            
            if game_choice == "1":
                game_file = leaderboard_number
                profile_file = user_profile_number
            elif game_choice == "2":
                game_file = leaderboard_adventure
                profile_file = user_profile_adventure
            
            score = int(input("Enter your score: "))
            save_to_profile(username, profile_file, score)
            compare(game_file, username, score)
            
            # reload and delete 
            scores = load_high_scores(game_file)
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]  # Keep top 10
            save_high_scores(game_file, dict(sorted_scores))
        
        elif choice == "2":
            print("Select game:")
            print("1. Number guessing Game")
            print("2. Text adventure Game")
            game_choice = input("Enter your choice (1-2) ")
            
            if game_choice == "1":
                print_leaderboard(leaderboard_number, "Number guessing game")
            elif game_choice == "2":
                print_leaderboard(leaderboard_adventure, "Text adventure game")
        
        elif choice == "3":
            username = input("Enter the username to view scores: ")
            print("Select game:")
            print("1. Number guessing game")
            print("2. Text adventure game")
            game_choice = input("Enter your choice (1-2): ")
            
            if game_choice == "1":
                print_user_scores(username, user_profile_number, "Number guessing game")
            elif game_choice == "2":
                print_user_scores(username, user_profile_adventure, "Text adventure game")
            else:
                print("Invalid choice")
                continue
        
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
"""
import csv

scores={}

# Loading scores 
def load_high_scores(game_file):
    with open(game_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                scores[row[0]] = int(row[1])
    return scores

#save scores to the csv 
def save_high_scores(game_file, scores):
    with open(game_file, "w", newline="") as file:
        writer = csv.writer(file)
        for user, score in scores.items():
            writer.writerow([user, score])

#saving to profile 
def save_to_profile(username, profile_file, score):
    with open(profile_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

#compare scores and update 
def compare(game_file, username, score):
    scores = load_high_scores(game_file)
    if username in scores:
        if score > scores[username]: 
            scores[username] = score
    else:
        scores[username] = score
    save_high_scores(game_file, scores)
#printing for all user scores
def print_user_scores(username, profile_file, game_name):
    with open(profile_file, "r") as file:
        reader = csv.reader(file)
        print(f"Scores for {username} in {game_name}:")
        for row in reader:
            if row[0] == username:
                print(f"Score: {row[1]}")


if __name__ == "main"
    compare(game_file, username, score)
    save_to_profile(username, profile_file, score)
    save_high_scores(game_file, scores)
    load_high_scores(game_file)
    print_user_scores(username, profile_file, game_name)
    

