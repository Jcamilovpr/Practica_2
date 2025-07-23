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

user_number = 1
while user_number != 0:
    user_number = int(input("Tell me a number, 0 to stop: "))
    print(f"You told me the number {user_number}")
print("you stop the program.")

# Exercise 7: Functions - Factorial
# Write a function to calculate the factorial of a number.


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"{number} factorial is: {result}")


factorial(5)

# Exercise 8: Classes - Person Object
# Define a class `Person` with attributes `name` and `age` and a method to introduce the person.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"Hello {self.name}, you are {self.age} years old.")


person_1 = Person("Camilo", 25)
person_1.saludar()

# Exercise 9: List Filtering
# Given a list of numbers, create a new list with only even numbers.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for n in numbers:
    if n % 2 == 0:
        new_list.append(n)

print(new_list)

# Exercise 10: String Reverse
# Write a function that reverses a string.


def inverted(word):
    word = "".join(reversed(word))
    return word


print(inverted("camilo"))
