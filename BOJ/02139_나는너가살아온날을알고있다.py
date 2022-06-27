from datetime import datetime, timedelta
while(True):
    day, month, year = map(int, input().split(' '))
    if (day == 0 and month == 0 and year == 0):
        break
    else:
        t_1 = datetime(year, month, day)
        t_2 = datetime(year, 1, 1)
        print((t_1 - t_2).days+1)
