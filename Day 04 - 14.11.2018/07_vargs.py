def print_params(msg, *numbers, **pairs):
    print("msg",msg)
    print("numbers",numbers)
    print("pairs",pairs)


print_params("hello",1,2,3,4,"TEST",name="bob",age=13)

"""
OUTPUT:
_______________
msg hello
numbers (1, 2, 3, 4, 'TEST')
pairs {'name': 'bob', 'age': 13}
"""
