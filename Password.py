import random

print("Welcome to the Password Generator!")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=[]{}/<>~"

all_characters = letters + numbers + symbols

length = input("Enter the length of your password: ")
length = int(length)

password = ""

for i in range(length):
    password = password + random.choice(all_characters)

print("Here is your new password:", password)
