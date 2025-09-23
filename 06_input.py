magic_num = 0

while magic_num != 80:
    magic_num = int(input("What is the Magic Number? "))


user_input = input("\nPlease enter a new number: ")
print(f"You entered: {user_input} with a variable type of: {type(user_input)}")
print("The input() method always creates a string.")
print(f"We can convert that to an int with int(user_input): {int(user_input)}")
