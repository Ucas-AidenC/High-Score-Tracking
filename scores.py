import csv

# Dictionary for storing scores
scores = {}

# File paths for leaderboards and user profiles
leaderboard_number = "guessing_game.csv"
leaderboard_adventure = "text_adventure.csv"
user_profile_number = "user_profiles_number_guessing.csv"
user_profile_adventure = "user_profiles_text_adventure.csv"

# Load scores from a CSV file
def load_high_scores(game_file):
    leaderboard = []
    try:
        with open(game_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 3:  # Ensure correct format
                    leaderboard.append([int(row[1]), row[2]])  # Store as [score, username]
    except (FileNotFoundError, ValueError):
        pass  # If file doesn't exist or has invalid data, start fresh
    return leaderboard

def save_high_scores(game_file, leaderboard):
    for i in range(len(leaderboard) - 1):
        for j in range(i + 1, len(leaderboard)):
            score_i, time_i = leaderboard[i]
            score_j, time_j = leaderboard[j]

            if score_i < score_j or (score_i == score_j and time_i > time_j):
                leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]
    
    if len(leaderboard) > 10:
        leaderboard = leaderboard[:10]  # Keep only top 10
    
    with open(game_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["place", "score", "user"])  # Write header
        place = 1
        for entry in leaderboard:
            writer.writerow([place, entry[0], entry[1]])
            place += 1

# Save user score to profile history
def save_to_profile(username, profile_file, score):
    with open(profile_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

# Compare scores and update the leaderboard
def compare(game_file, username, score):
    leaderboard = load_high_scores(game_file)
    leaderboard.append([score, username])  # Append new score
    save_high_scores(game_file, leaderboard)

# Print user scores from profile history
def print_user_scores(username, profile_file, game_name):
    try:
        with open(profile_file, "r") as file:
            reader = csv.reader(file)
            print(f"Scores for {username} in {game_name}:")
            for row in reader:
                if row[0] == username:
                    print(f"Score: {row[1]}")
    except FileNotFoundError:
        print("No scores found.")

if __name__ == "__main__":
    compare(leaderboard_adventure, "test_user", 150)
    save_to_profile("test_user", user_profile_adventure, 150)
    print_user_scores("test_user", user_profile_adventure, "Adventure Game")