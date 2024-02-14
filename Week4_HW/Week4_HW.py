'''
# Car's numbers are separate from False numbers
tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1)

# How do only do a set number to show
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:6])

# How to change a number in a list
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)

# How to change a number in a multy list
tuple1 = (11, [64, 33], 243, 123)
tuple1[1][1] = 66
print(tuple1)

# Remove duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
sets = set1.union(set2)
print(sets)

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()
odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)
even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)
print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

list1 = [34, 54, 67, 89, 11, 43, 94]
element = list1.pop(4)
list1.insert(2, element)
list1.append(element)
print("List after Adding element at last ", list1)

list1 = [10, 20, [300, 400, [5000, 6000],500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)

list1 = ["a", "b",["c",["d", "e", ["f", "g"], "k"],"l"],"m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

tuple1 = (40, 19, 234, 12, 10, 123)
tuple1 = tuple1[::-1]
print(tuple1)
'''
dict1 = {
    "course": {
        "students": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(dict1["course"]["students"]["marks"]["history"])
