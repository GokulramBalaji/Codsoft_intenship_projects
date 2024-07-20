import random
import string
while True:

    n=int(input("Enter the desired length of the password  :"))
    def generate_password(length=n):
           characters = string.ascii_letters + string.digits + string.punctuation
           password = ''.join(random.choice(characters) for _ in range(length))
           return password
    desired_length =n
    generated_password = generate_password(desired_length)
    print(f"Generated password: {generated_password}")

