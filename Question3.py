import operator
myList = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
myKey = "color"
def sortList(myList,myKey):
    return (sorted(myList,key=operator.itemgetter(myKey)))
print(sortList(myList,myKey))