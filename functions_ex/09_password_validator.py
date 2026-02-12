def valid_password(password):
    is_valid = True
    counter_digits = 0
    for char in password:
        if char.isdigit():
            counter_digits += 1
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    if not counter_digits >= 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


password_ = input()

valid_password(password_)