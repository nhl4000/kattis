import datetime
[D, M] = list(map(int, raw_input().split()))
print(datetime.date(2009, M, D).strftime('%A'))
