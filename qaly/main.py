periods = int(input())
q = []
for _ in range(periods):
    [q_temp , y_temp] = list(map(float, raw_input().split()))
    q.append(q_temp*y_temp)
print(sum(q))
