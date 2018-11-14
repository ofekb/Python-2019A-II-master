arr=["ab","cd"]

for singleString in arr:
    print("The word", singleString, "contains this chars:")
    for singleChar in singleString:
        print(singleChar)

"""
The word ab contains this chars:
a
b
The word cd contains this chars:
c
d
"""