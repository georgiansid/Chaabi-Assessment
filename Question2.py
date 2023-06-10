myInput = input()
def returnTypeDict(arr,typeDict):
    returnDict = {}
    for i in range(len(arr)):
        arr[i] = arr[i].split(".")
    for i in range(len(arr)):
        if len(arr[i]) == 1:
            returnDict[arr[i][0]] = "unknown"
        elif arr[i][1] not in typeDict:
            returnDict[arr[i][0] + "." + arr[i][1]] = "unknown"
        else:
            returnDict[arr[i][0] + "." + arr[i][1]] = typeDict[arr[i][1]]
    return returnDict
myInput = myInput.split(";")
extDict = {}
for i in range(len(myInput)):
    myInput[i] = myInput[i].split(",")
for i in range(len(myInput)):
    extDict[myInput[i][0]] = myInput[i][1]
arr = ["abc.jpg","xyz.xls", "text.csv", "123"]
print(returnTypeDict(arr,extDict))