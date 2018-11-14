person={
    "id":1
}

name=""


# WHILE RUNS WHEN THE CONDITION RETURNS TRUE
while len(name)<3:
    name=input("insert name (min 3 chars)")
# WHEN THE LOOP IS DONE - THE "else" PART RUNS ONE TIME
else:
    person["name"]=name


age=-1

while age<0 or age>120:
    age=int(input("insert age (0-120)"))
else:
    person["age"]=age


print("-----------person with valid details:-----------")
print(person)


"""
OUTPUT:
________________________
insert name (min 3 chars)bo
insert name (min 3 chars)bob
insert age (0-120)-5
insert age (0-120)130
insert age (0-120)20
-----------person with valid details:-----------
{'id': 1, 'name': 'bob', 'age': 20}
"""
