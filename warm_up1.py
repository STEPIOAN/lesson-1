# Ask the user for input
username = input("Enter username: ")

# Store a string in a variable
favorite_color = "Blue"
name = "Alex"

# Combine strings using + and f-strings
print("Hello " + name + "!")
print(f"Hello {username}, your favorite color could be {favorite_color}!")

# If / Else example
user_color = input("What is your favorite color? ")

if user_color == favorite_color:
    print("Wow! We both like the same color!")
else:
    print(f"Nice! {user_color} is a great color too!")
