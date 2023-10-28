import random

def calculate_love_compatibility():
    # Generate a random "love compatibility" score between 1 and 100.
    return random.randint(1, 100)

def main():
    print("Welcome to the Love Calculator!")
    player_name = input("Enter your name: ")
    crush_name = input("Enter the name of your crush: ")
    
    love_score = calculate_love_compatibility()

    print(f"\nCalculating love compatibility between {player_name} and {crush_name}...")
    print(f"Love Compatibility: {love_score}%\n")

    if love_score > 70:
        print(f"{player_name} and {crush_name} are a great match! Love is in the air.")
    elif love_score > 30:
        print(f"{player_name} and {crush_name} have a chance. Keep trying!")
    else:
        print(f"{player_name} and {crush_name} are not meant to be. Maybe next time.")

if __name__ == "__main__":
    main()
