# Branden Wilkins
# UWYO COSC 1010
# 10/29/2024
# Lab 07
# Lab Section: 11 
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

while True:
    User_Input = input("please input a upper bound: ")
    if User_Input.isdigit() and int(User_Input) > 0:
        User_Input = int(User_Input)
        factorial = 1
        for i in range(1, User_Input + 1):
            factorial *= i
        print(f"The result of the factorial based on the given bound is {factorial}")
        break
    else:
        print("please give me a valid upper bound")
    

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 
while True:
    User_Num = input("please give me a number: ")
    if User_Num.lower() == "exit":
        break
    elif User_Num[0] == "-" and User_Num[0:].replace("-","").isdigit():
        num_sum += int(User_Num)
    elif User_Num.isdigit():
        num_sum += int(User_Num)
    else:
        print("please give me a valid number")
print(f"your final sun is {num_sum}")   

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

while True:
    User_Problum = input("please give me a equation: ")
    if User_Problum.lower() == "exit":
        break
    for symble in ["+","-","%","/","*"]:
        if (symble in User_Problum):
            problum = User_Problum.split(symble)
            part1 = problum[0].replace(" ","")
            part2 = problum[1].replace(" ","")
            if part1.isdigit() and part2.isdigit():
                part1 = int(part1)
                part2 = int(part2)
                if symble == '+':
                    answer = part1 + part2
                elif symble == '-':
                    answer = part1 - part2
                elif symble == '/':
                    answer = part1 / part2
                elif symble == '*':
                    answer = part1 * part2
                elif symble == '%':
                    answer = part1 % part2
                print(f"The answer is: {answer}")
                break
    else:
        print("please imput a valid problum")

        