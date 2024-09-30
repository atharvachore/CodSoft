import random
import string

def generate_password(length):
    # Define the characters to use for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for the password length
try:
    length = int(input("Enter the desired length for the password: "))
    if length < 1:
        print("Password length should be at least 1.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated password: {password}")
except ValueError:
    print("Please enter a valid number.")
