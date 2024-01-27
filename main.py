
import user_data
from user_manager import login, login_messages

def main():
    users = user_data.load_users()

    user_name = input("Enter your name: ")
    message, current_user = login(users, user_name)

    login_messages(users, message, current_user)

    user_data.save_users(users)

if __name__ == "__main__":
    main()

