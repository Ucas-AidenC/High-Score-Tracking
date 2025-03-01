import csv

# Code by Aiden

# Dictionary for storing high scores (key: username, value: highest score)
scores_dict = {}

# Load scores from a CSV file into the dictionary
def load_high_scores(game_file):
    global scores_dict
    scores_dict = {}  # Reset dictionary before loading

    try:
        with open(game_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 2:  # Ensure correct format
                    username = row[0]
                    score = int(row[1])
                    scores_dict[username] = score
    except (FileNotFoundError, ValueError):
        pass  # If file doesn't exist or has invalid data, start fresh

# Save the dictionary of high scores to a CSV file
def save_high_scores(game_file):
    with open(game_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["user", "score"])  # Header
        for username, score in scores_dict.items():
            writer.writerow([username, score])

# Compare scores, update both dictionary and CSV
def compare(game_file, username, score):
    load_high_scores(game_file)  # Load current scores into dictionary

    # Only update if the new score is higher
    if username in scores_dict:
        if score > scores_dict[username]:
            scores_dict[username] = score
    else:
        scores_dict[username] = score  # New entry

    save_high_scores(game_file)  # Save updated dictionary to CSV

# Ensure dictionary is updated immediately when loading scores elsewhere
def update_dictionary_from_csv(game_file):
    load_high_scores(game_file)

# Example usage
if __name__ == "__main__":
    compare("text_adventure.csv", "test_user", 150)
    print(scores_dict)  # Debugging: Print updated dictionary
