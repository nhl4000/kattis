import math
[h, v] = list(map(int, raw_input().split()))
print(int(math.ceil(float(h) / math.sin(math.radians(v)))))