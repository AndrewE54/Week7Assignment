import random
import string

# Added special characters to create stronger passwords.
characters = string.ascii_letters + string.digits + string.punctuation

length = 16
password = "".join(random.choice(characters) for _ in range(length))

print("Generated password:", password)

# Check the password length and confirm it was generated successfully.
print("Password length:", len(password))
print("Password generation complete.")
