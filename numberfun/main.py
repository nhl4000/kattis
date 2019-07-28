ans = []
n = int(raw_input())
for _ in range(n):
    [a, b, c] = list(map(int, raw_input().split()))
    bPossible = False
    if ((a + b) == c):
        bPossible = True
    if ((a - b) == c) or ((b - a) == c):
        bPossible = True
    if ((a * b) == c):
        bPossible = True
    if ((float(a) / float(b)) == c) or ((float(b) / float(a)) == c):
        bPossible = True
    ans.append(bPossible)

for i in ans:
    if (i):
        print("Possible")
    else:
        print("Impossible")