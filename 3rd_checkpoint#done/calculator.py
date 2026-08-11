# The objective is to create a simple calculator application in Python that can perform basic arithmetic operations such as addition
# subtraction, multiplication, and division.
# Description:
# This exercise involves creating a simple calculator app using Python. The app should be able to perform addition, subtraction, multiplication,
# and division operations. It will prompt the user to input two numbers and an arithmetic operator,
# then perform the corresponding operation on the numbers and return the result.
# Example :
# Input:
# Enter the first number: 10
# Enter the second number: 5
# Enter the operator (+, -, *, /): *
# Output:
# The result is: 50
# Instructions
# Open a new Python file in your preferred code editor.
# Define a function called "calculator" that takes two arguments, "num1" and "num2".
# Within the function, prompt the user to enter an operator (+, -, *, /).
# Use conditional statements to determine which operation to perform based on the user's input.
# Return the result of the operation.
# Call the function calculator with two numbers and print the result.
# Handle cases where the user inputs invalid operators or tries to divide by zero.
# Note: 
# You may want to use a "while" loop to allow the user to roll the dice multiple times, or to add some messages to make the program more user-friendly.

while True:

 

 

 



 def calculator(num1,operator1,num2):

    listop =["+" , "-" , "*","/"]

    while operator1 not in listop:

        print('\nThe operator MUST be one of those : " + "" or " - " or " * " or " /" .')

        operator1 = input('\nRe-input the operator :')

    while num2==0 and operator1 =="/" :

     print("Error ! You can't divide by a zero")

     num2 = float(input("Input the 2nd number (It must not be a zero ) : "))

    result = num1 + num2 if operator1 == "+" else num1 - num2 if operator1 == "-" else num1 * num2 if operator1 == "*" else num1 / num2 if operator1 == "/" else ...

    return f"{num1} {operator1} {num2} = {result}"

 print(calculator(float(input("Input the 1st number : ")),input('Input one of these operators: " + "" or " - " or " * " or " /" :   '),float(input("Input the 2nd number : "))))



 opinion = input("Do you want to exit : Yes / No?\n ").upper()

 while opinion != "YES" and opinion != "NO":

  print("\n Please enter only : Yes or NO : ")

  opinion = input("\n Do you want to exit : Yes / No? \n").upper()

 if opinion =="YES":

   break

 elif opinion =="NO":

   pass 
#Done