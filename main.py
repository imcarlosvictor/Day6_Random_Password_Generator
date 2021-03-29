import string
import random
from typing import List

LOWERCASE: str = string.ascii_lowercase
UPPERCASE: str = string.ascii_uppercase
NUMBERS: str = string.digits
SYMBOLS: str = string.punctuation

pw_length: int = 0

# Step 1: Find password length
find_length = True
while find_length:

    try:
        pw_length: int = int(input('Enter password length: '))
    except ValueError:
        print('Enter a number.')

    if pw_length >= 6:
        find_length = False
    else:
        print('Password length must be greater than 6.')

# Step 2: Find parameters for password
print('\n')
print("""1. Lowercase
2. Uppercase
3. Numbers
4. Symbols
""")

password_parameters: str = input(
    'Enter password parameters (e.g. 1 2 4): ').split()

# Convert input into integers
pw_params = map(int, password_parameters)
pw_params: List[int] = list(pw_params)

generate_password = True
while generate_password:

    # Include chosen parameters in password
    user_parameters: str = ''

    if 1 in pw_params:
        user_parameters += LOWERCASE

    if 2 in pw_params:
        user_parameters += UPPERCASE

    if 3 in pw_params:
        user_parameters += NUMBERS

    if 4 in pw_params:
        user_parameters += SYMBOLS

    # Generate a password
    user_password: List[str] = random.sample(user_parameters, pw_length)
    user_password: str = ''.join(user_password)
    print(f'New password: {user_password}')

    # Ask if user wants to generate a new password
    try_again = True
    while try_again:

        user_try: str = input(
            'Generate new password with the same parameters? (y/n): ')

        if user_try == 'n':
            generate_password = False
            try_again = False
        elif user_try == 'y':
            print('Generating...')
            try_again = False
        else:
            print("Enter 'y' or 'n'.")
