[n, m] = list(map(int, raw_input().split()))
sums = {}
for x in range(1, n + 1):
    for y in range(1, m + 1):
        sum_temp = x + y
        if sum_temp in sums:
            sums[sum_temp] += 1
        else:
            sums[sum_temp] = 1

maxP = 0
ans = []
for k,s in sums.items():
    if s > maxP:
        maxP = s
        ans = [k]
    elif (s == maxP):
        ans.append(k)
    
print("\r\n".join(list(map(str, ans))))

