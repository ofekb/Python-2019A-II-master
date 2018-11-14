# `input` function returns the user input as a string
age = int(input("Enter your age: "))

if age>0 and age<120:
    if age<18:
        print("To young...")
        print("You can buy soft drink...")
    else:
        print("To old...")
        print("You can buy wine...")

print("your age is",age)

"""
Example 1 of program execution:
___________________________________

Enter your age: 200
your age is 200

"""

"""
Example 2 of program execution:
___________________________________

Enter your age: 22
To old...
You can buy wine...
your age is 22
"""

"""
Example 3 of program execution:
___________________________________

Enter your age: 13
To young...
You can buy soft drink...
your age is 13
"""