import csv
#def dictoranry for updating 
scores={}

#varibles used in place of file paths 
leaderboard_number = "guessing_game.csv"
leaderboard_adventure = "text_adventure.csv"
user_profile_number = "user_profiles_number_guessing.csv"
user_profile_adventure = "user_profiles_text_adventure.csv"



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
    
