import user_data
from coin_flip_game import play_coin_flip_game

def game_loop(users, current_user):
    while True:
        command = input("Enter a command (flip [amount] [heads/tails]/exit): ").lower()
        if command == "exit":
            break
        elif command.startswith("flip "):
            response = process_flip_command(users, current_user, command)
            print(response)
            if "has been removed" in response:
                break  # Exit the loop if the user has been removed
        else:
            print("Unknown command.")

def process_flip_command(users, current_user, command):
    try:
        parts = command.split()
        bet_amount = int(parts[1])
        guess = parts[2]

        if guess not in ["heads", "tails"]:
            return "Invalid guess. Please choose 'heads' or 'tails'."

        # Move the coin flip animation call to inside play_coin_flip_game

        result_message, success = play_coin_flip_game(current_user, bet_amount, guess)
        
        if current_user.coins <= 0:
            del users[current_user.name]
            user_data.save_users(users)
            return f"{result_message}\nUser {current_user.name} has been removed due to insufficient coins."

        return result_message

    except (IndexError, ValueError):
        return "Invalid command or amount."
