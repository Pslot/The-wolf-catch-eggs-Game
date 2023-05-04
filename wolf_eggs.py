import random
import time
import os

# Set up the game
score = 0
rounds = 1
max_rounds = 5
best_score = 0

# Set up the game difficulty levels
difficulty_levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}

# Set up the game styling
EGG_CHAR = "o"
WOLF_CHAR = "W"
BG_CHAR = "*"
STYLE = {
    "easy": {
        "egg_color": "\033[1;33;40m",
        "wolf_color": "\033[1;31;40m",
        "bg_color": "\033[1;32;40m",
        "text_color": "\033[1;37;40m",
        "score_text": "Eggz: "
    },
    "medium": {
        "egg_color": "\033[1;35;40m",
        "wolf_color": "\033[1;34;40m",
        "bg_color": "\033[1;36;40m",
        "text_color": "\033[1;37;40m",
        "score_text": "Eggz: "
    },
    "hard": {
        "egg_color": "\033[1;31;40m",
        "wolf_color": "\033[1;30;40m",
        "bg_color": "\033[1;33;40m",
        "text_color": "\033[1;37;40m",
        "score_text": "EGGZ: "
    }
}

# Define the egg and wolf classes
class Egg:
    def __init__(self, x):
        self.x = x
        self.y = 0
    
    def move(self):
        self.y += 1
    
    def draw(self, egg_color):
        print(" " * self.x + egg_color + EGG_CHAR + "\033[0m")
    
class Wolf:
    def __init__(self):
        self.x = 0
    
    def move(self):
        self.x += random.choice([-1, 1])
    
    def draw(self, wolf_color):
        print(" " * self.x + wolf_color + WOLF_CHAR + "\033[0m")

# Game loop
while rounds <= max_rounds:
    print("\033[2J\033[H") # clear the screen
    print("\033[1;37;40m" + "-" * 30 + "\033[0m") # print separator
    
    # Get the game difficulty level from the player
    print("\033[1;37;40m" + "Difficulty levels:" + "\033[0m")
    for level in difficulty_levels.keys():
        print("\033[1;37;40m" + f"- {level.title()} ({difficulty_levels[level]})" + "\033[0m")
    level_input = input("\033[1;37;40m" + "Enter the difficulty level: " + "\033[0m")
    while level_input not in difficulty_levels.keys():
        level_input = input("\033[1;37;40m" + "Invalid input. Enter the difficulty level: " + "\033[0m")
    difficulty_level = level_input
    egg_speed = difficulty_levels[difficulty_level]
    
    # Print the current and best score
    print(f"\033[1;37;40mCurrent score: {score}\033[0m")
    print(f"\033[1;37;40mBest score: {best_score}\033[0m")
    print("\033[1;37;40m" + "-" * 30 + "\033[0m")
    
    # Create a list of eggs and the wolf
    eggs = []
    wolf = Wolf()
    
    # Game loop for each round
    round_score = 0
    while True:
        # Spawn a new egg
        if random.random() < 0.5:
            eggs.append(Egg(random.randint(0, 29)))
        
        # Move and draw the eggs
        for egg in eggs:
            egg.move()
            egg.draw(STYLE[difficulty_level]["egg_color"])
            
            # If the egg falls off the screen
            if egg.y > 20:
                eggs.remove(egg)
        
        # Move and draw the wolf
        wolf.move()
        wolf.draw(STYLE[difficulty_level]["wolf_color"])
        
        # Check if the wolf catches the egg
        for egg in eggs:
            if egg.y == 20 and egg.x == wolf.x:
                eggs.remove(egg)
                round_score += 1
                score += 1
                print(f"\033[1;37;40m{STYLE[difficulty_level]['score_text']}{score}\033[0m")
        
        # Check if the game is over
        if round_score >= 5 or len(eggs) >= 10:
            break
        
        # Wait for a short time
        time.sleep(1 / egg_speed)
    
    # Print the end-of-round message and update the best score
    if round_score >= 5:
        print("\033[1;32;40mYou win!\033[0m")
        if score > best_score:
            best_score = score
    else:
        print("\033[1;31;40mYou lose!\033[0m")
    
    # Wait for the player to start the next round
    input("\033[1;37;40mPress Enter to start the next round.\033[0m")
    
    # Update the round count
    rounds += 1

print("\033[2J\033[H") # clear the screen
print("\033[1;37;40m" + "-" * 30 + "\033[0m")
print("\033[1;37;40m" + "Game over!" + "\033[0m")
print(f"\033[1;37;40mYour score: {score}\033[0m")
print(f"\033[1;37;40mBest score: {best_score}\033[0m")
print("\033[1;37;40m" + "-" * 30 + "\033[0m")


# I want you to note that this code includes styling and colored output, so it may not work on all terminals.