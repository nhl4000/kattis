import math
[n, w, h] = list(map(int, raw_input().split()))
limit = math.sqrt(w*w + h*h)
ans = []
for _ in range(n):
    x = int(raw_input())
    if (x <= limit):
        ans.append("DA")
    else:
        ans.append("NE")

for a in ans:
    print(a)
