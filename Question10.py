from datetime import datetime, timedelta
def get_previous_date(date, n):
    myDate = datetime.strptime(date, '%y-%m-%d')
    prevDate = myDate - timedelta(days=n)
    prevDateStr = prevDate.strftime('%y-%m-%d')
    return prevDateStr
date = '16-12-10'
prevTime = 11
print(get_previous_date(date,prevTime))