counter=0

while counter<4:
    counter+= 1
    if counter==2:
        continue
    print("in loop",counter)

else:
    print("after loop",counter)



"""
in loop 1
in loop 3
in loop 4
after loop 4
"""