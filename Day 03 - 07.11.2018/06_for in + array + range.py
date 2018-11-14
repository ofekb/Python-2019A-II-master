arr=["a","b","c","d"]

print("------------Regular for-in-----")
for x in arr:
    print("for-in",x)

print("------------Range for-in-----")
for x in range(0,len(arr)):
    print("for-in",x,arr[x] )

"""
OUTPUT:
________________
rray + range.py'
------------Regular for-in-----
for-in a
for-in b
for-in c
for-in d
------------Range for-in-----
for-in 0 a
for-in 1 b
for-in 2 c
for-in 3 d
"""