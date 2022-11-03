import datetime
payday = datetime.date(year=2022, day = 31, month=10)
period = datetime.timedelta(days=14)
next_payday = payday + period
print(next_payday)
