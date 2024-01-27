import random
import time
import os



def display_ascii_animation(flip_result):
    frames = [f"ascii/frame{i}.txt" for i in range(1, 20)]
    final_frame = "ascii/frame14.txt" if flip_result == "heads" else "ascii/frame19.txt"

    # Define frame display times for a more dynamic effect
    frame_times = [0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.2, 0.21, 0.2, 0.18, 0.16, 0.14, 0.11, 0.10, 0.09, 0.08]

    # Loop through all frames with varying display times except the final frame
    for frame_time, frame in zip(frame_times[:-1], frames[:-1]):
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(frame, 'r') as file:
            print(file.read())
        time.sleep(frame_time)

    # Display the final result frame
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(final_frame, 'r') as file:
        print(file.read())
    time.sleep(1)


def play_coin_flip_game(user, bet_amount, guess):
    if bet_amount > user.coins:
        return "Insufficient coins for this bet.", False
    elif bet_amount <= 0:
        return "Invalid bet amount.", False

    flip_result = random.choice(["heads", "tails"])
    display_ascii_animation(flip_result)  # Play the animation with the actual result

    if flip_result == guess:
        user.coins += bet_amount  # User wins
        return f"It's {flip_result}! You won! Your new coin balance is {user.coins}.", True
    else:
        user.coins -= bet_amount  # User loses
        return f"It's {flip_result}! You lost! Your new coin balance is {user.coins}.", False
