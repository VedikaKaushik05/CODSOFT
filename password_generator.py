
import random
import string

print("===== Password Generator =====")

length = int(input("Enter the password length: "))

if length <= 0:
    print("Please enter a positive number.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)