n = int(raw_input())
ans = []
for _ in range(n):
    [b, p] = list(map(float, raw_input().split()))
    calbpm = float((60.0  * b) / p)
    difbpm = float(60.0 / p)
    ans.append(str(calbpm - difbpm)+" "+str(calbpm)+" "+str(calbpm + difbpm))

for i in ans:
    print(i)