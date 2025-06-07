import random
import string
print("Welcome to My Password Generator!")
length = input("Enter the length of the password (minimum 8): ")
while not length.isdigit() or int(length) < 8:
    print("Please enter a valid number (8 or more).")
    length = input("Enter the length of the password (minimum 8): ")
length = int(length)
include_upper = input("Include uppercase letters? (y/n): ")
include_lower = input("Include lowercase letters? (y/n): ")
include_numbers = input("Include numbers? (y/n): ")
include_symbols = input("Include symbols? (y/n): ")
characters = ''
if include_upper.lower() == 'y':
    characters += string.ascii_uppercase

if include_lower.lower() == 'y':
    characters += string.ascii_lowercase

if include_numbers.lower() == 'y':
    characters += string.digits

if include_symbols.lower() == 'y':
    characters += string.punctuation
if len(characters) == 0:
    print("You must select at least one type of character!")
    exit()
password = ''
for i in range(length):
    password += random.choice(characters)

print("\nYour generated password is:")
print(password)
