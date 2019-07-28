[h, m] = list(map(int, raw_input().split()))
print("%d %d" % ((((h*60 + m) - 45) / 60) % 24, ((h*60 + m) - 45) % 60))