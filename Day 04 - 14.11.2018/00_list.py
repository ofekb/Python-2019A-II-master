fruitsList= ["Apple","Banan","Melon", "Mango"]


# get length of list
print("fruitsList has", len(fruitsList) ," items")
print(fruitsList)

# edit element index 1 to "WaterMelon"
fruitsList[1] = "WaterMelon"
print(fruitsList)

# edit last element in the list to "PineApple"
fruitsList[len(fruitsList) -1]="PineApple"
print(fruitsList)

# add to the end of the list "Orange"
fruitsList.append("Orange")

# get length of list
print("fruitsList has", len(fruitsList) ," items")
print(fruitsList)

# Sort the array by alpha-betic order
fruitsList.sort()
print(fruitsList)

# remove the first element in the list
del fruitsList[0]

# get length of list
print("fruitsList has", len(fruitsList) ," items")
print(fruitsList)



"""
OUTPUT:
_________________________
fruitsList has 4  items
['Apple', 'Banan', 'Melon', 'Mango']
['Apple', 'WaterMelon', 'Melon', 'Mango']
['Apple', 'WaterMelon', 'Melon', 'PineApple']
fruitsList has 5  items
['Apple', 'WaterMelon', 'Melon', 'PineApple', 'Orange']
['Apple', 'Melon', 'Orange', 'PineApple', 'WaterMelon']
fruitsList has 4  items
['Melon', 'Orange', 'PineApple', 'WaterMelon']
"""