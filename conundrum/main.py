c = raw_input()
n = len(c)
ans = 0
for i in range(n):
    if (i % 3 == 0) and (c[i] != "P"):
        ans += 1
    elif (i % 3 == 1) and (c[i] != "E"):
        ans += 1
    elif (i % 3 == 2) and (c[i] != "R"):
        ans += 1
print(ans)