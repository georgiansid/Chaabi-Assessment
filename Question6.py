def dubList(arr, n,m):
    retArr = []
    for i in range(n,m+1,2):
        retArr.append(arr[i])
    return retArr
arr = [2,3,5,7,11,13,17,19,23,29,31,37,41]
startIndex = 2
endIndex = 9
print(dubList(arr, startIndex, endIndex))