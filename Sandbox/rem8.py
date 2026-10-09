def create_account():
    while True:
        username = input("Create your username: ")
        password = input("Create your password: ")

        if username and password:
            return username, password

        print("Username and password cannot be empty.")


def authenticate(username, password, username_attempt, password_attempt):
    if username_attempt == username and password_attempt == password:
        return True

    return False


def login(username, password):
    attempts = 0

    while attempts < 3:
        username_attempt = input("Enter your username: ")
        password_attempt = input("Enter your password: ")

        attempts += 1

        if authenticate(username, password, username_attempt, password_attempt):
            print(f"Welcome {username}!")
            return True

        print("Invalid username or password.")

    print("Too many attempts.")
    return False


username, password = create_account()

login(username, password)