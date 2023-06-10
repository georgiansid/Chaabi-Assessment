from_date = '98-11-12'
to_date = '94-11-12'
def differenceCalculator(fromDate,toDate,difference):
    fromArr = from_date.split('-')
    toArr = to_date.split('-')
    yrDiff = int(toArr[0])-int(fromArr[0])
    monDiff = int(toArr[1])-int(fromArr[1])
    dayDiff = int(toArr[2])-int(fromArr[2])
    if (abs(yrDiff)*365 + abs(monDiff)*30 + abs(dayDiff)) < difference:
        return True
    else:
        return False
print(differenceCalculator(from_date,to_date,1900))