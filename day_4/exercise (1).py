# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.
import math

def calculate():
    operation = input('''
Please tyoe in the math operationyou would like to complete:
+ for addition
- for subtraction
* for multiplication
''')


# Easy:
#     - A function that subtracts one integer from another
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if operation == '+':
    print('{} + {} = '.format(num1, num2))
print(num1 + num2)


def sub(num1, num2):
    return num1-num2
print()
#     - A function that multiplies three integers
#number_1 = int(input('ENter first number: '))
#number_2 = int(input('Enter second number: '))
#number_3 = int(input('Enter your third number: '))
# print(number_1 * number_2 * number_3)

def mult_three_nums(num1, num2, num3):
    return num1 * num2 * num3

#     - A function that adds four integers

def add_four_nums(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    return sum 


# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

#def calculator():
    #first_number = float(int(input("first number:"))
    #type_of_operation = input("please choose: +, -, *, /: ")
    #second_number = float(input("second number: "))

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.
