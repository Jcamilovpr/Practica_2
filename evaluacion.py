# Exercise 1: Variables and Operators
# Write a Python program to define two numbers and print their sum, difference, product, and quotient.
number_1 = int(input("Give me a number:"))
number_2 = int(input("Give me another number:"))

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2)

# Exercise 2: String Manipulation
# Write a Python program to take a user's name as input and print a greeting message.

name = input("What is your name? ")
print(f"Hello {name}, welcome to your repository!")

# Exercise 3: List Operations
# Create a list of five numbers and print the maximum and minimum values from the list.

numbers = [1, 5, 6, 10, 8]
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

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
print(f"the total is: {total}")

# Exercise 6: While Loop
# Write a program that asks the user for numbers and stops when they enter 0.


# Exercise 7: Functions - Factorial
# Write a function to calculate the factorial of a number.


# Exercise 8: Classes - Person Object
# Define a class `Person` with attributes `name` and `age` and a method to introduce the person.


# Exercise 9: List Filtering
# Given a list of numbers, create a new list with only even numbers.


# Exercise 10: String Reverse
# Write a function that reverses a string.
