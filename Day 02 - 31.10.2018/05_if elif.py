# `input` function returns the user input as a string
age = int(input("Enter your age: "))

if age<0:
    print("Invalid age...")
elif age<18:
    print("To young...")
    print("You can buy soft drink...")
else:
    print("To old...")
    print("You can buy wine...")

print("your age is",age)


"""
Example 1 of program execution:
___________________________________

Enter your age: -2
Invalid age...
your age is -2
"""

"""
Example 2 of program execution:
___________________________________

Enter your age: 15
To young...
You can buy soft drink...
your age is 15
"""

"""
Example 3 of program execution:
___________________________________
Enter your age: 20
To old...
You can buy wine...
your age is 20
"""