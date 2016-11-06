from datetime import date
from datetime import timedelta
​
​
def checkio(from_date, to_date):
    count = 0
    cur_date = from_date
    while cur_date <= to_date:
        if cur_date.weekday() == 5 or cur_date.weekday() == 6:
            count += 1
        cur_date += timedelta(days=1)
    return count
