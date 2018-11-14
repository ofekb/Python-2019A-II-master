#Non-default argument can not be followed by default argument
def say_msg(msg, times=2):
    print((msg+" ")*times)


say_msg("welcome")
say_msg("hello",3)


"""
OUTPUT:
__________________________
welcome welcome
hello hello hello
"""