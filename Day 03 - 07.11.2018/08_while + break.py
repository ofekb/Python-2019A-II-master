counter=0

while counter<10:
    print("in loop",counter)
    if counter==5:
        break
    counter+= 1
else:
    print("after loop",counter)



"""
OUTPUT:
in loop 0
in loop 1
in loop 2
in loop 3
in loop 4
in loop 5
"""