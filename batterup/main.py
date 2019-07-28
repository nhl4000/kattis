n = int(raw_input())
hits = list(map(int, raw_input().split()))
s = []
for hit in hits:
    if (hit == -1):
        continue
    s.append(hit)

print(float(sum(s))/float(len(s)))