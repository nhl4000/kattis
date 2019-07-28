t = int(raw_input())
ans = []
for _ in range(t):
    n_cities = int(raw_input())
    s = set()
    for _ in range(n_cities):
        s.add(raw_input())
    ans.append(len(s))

for i in ans:
    print(i)
