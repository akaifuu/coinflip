from user import User
import user_data
from game_manager import game_loop

def create_user(name):
    return User(name)


def login(users, user_name):
    if len(user_name) < 2:
        return "Username too short", None

    if user_name in users:
        return "Welcome back", users[user_name]
    else:
        new_user = create_user(user_name)
        users[user_name] = new_user
        user_data.save_users(users)
        return "Account created", new_user
    

def login_messages(users, message, current_user):
    if current_user:
        print(f"{message}, {current_user.name}")
        if message == "Welcome back":
            print(f"Logged in successfully. Coins: {current_user.coins}")
        elif message == "Account created":
            print(f"Starting credit: {current_user.coins} coins.")
        game_loop(users, current_user)
    else:
        print(message)