# Exercise 1: Variables and Operators
# Write a Python program to define two numbers and print their sum, difference, product, and quotient.
Number_1 = int(input("Give me a number:"))
Number_2 = int(input("Give me another number:"))

print(Number_1 + Number_2)
print(Number_1 - Number_2)
print(Number_1 * Number_2)
print(Number_1 % Number_2)

# Exercise 2: String Manipulation
# Write a Python program to take a user's name as input and print a greeting message.

Name = input("What is your name? ")
print(f"Hello {Name}, welcome to your repository!")

# Exercise 3: List Operations
# Create a list of five numbers and print the maximum and minimum values from the list.

numbers = [1, 5, 6, 10, 8]
print(max(numbers))
print(min(numbers))


# Exercise 4: If Statement
# Write a Python program that checks if a number is positive, negative, or zero.

number = int(input("Give me a number:"))
if number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")

# Exercise 5: Loop - Sum of Numbers
# Write a Python program to calculate the sum of numbers from 1 to 10 using a loop.

total = 0
for n in range(1, 11):
    total += n
    print(total)
