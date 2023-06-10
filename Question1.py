def driverFunction(myArr):
    for i in range(len(myArr)):
        minIndex = i
        for j in range(i+1,len(myArr)):
            if (myArr[i] < myArr[minIndex]):
                minIndex = j
        myArr[i], myArr[minIndex] = myArr[minIndex], myArr[i]
    return myArr