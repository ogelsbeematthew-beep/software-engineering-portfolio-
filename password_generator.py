import random
import string

print("Password Generator")

length = int(input("How many characters should the password have? "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
