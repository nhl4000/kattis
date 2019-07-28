[x1, y1] = list(map(int, raw_input().split()))
[x2, y2] = list(map(int, raw_input().split()))
[x3, y3] = list(map(int, raw_input().split()))

ans = []
x = [x1, x2, x3]
y = [y1, y2, y3]

if (x.count(x1) == 2):
    if (x.count(x2) == 2):
        ans.append(str(x3))
    elif (x.count(x3) == 2):
        ans.append(str(x2))
else:
    ans.append(str(x1))

if (y.count(y1) == 2):
    if (y.count(y2) == 2):
        ans.append(str(y3))
    elif (y.count(y3) == 2):
        ans.append(str(y2))
else:
    ans.append(str(y1))

print(" ".join(ans))