def invertDict(dict):
    return ({value: key for key, value in dict.items()})
myDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
print(invertDict(myDict))