c = float(raw_input())
l = int(raw_input())
s = 0.0
for _ in range(l):
    [w, l] = list(map(float, raw_input().split()))
    s += float(float(w * l) * c)
print(s)