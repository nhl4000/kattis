[L, x] = list(map(int, raw_input().split()))
c = 0
hold = 0
for _ in range(x):
    [a, n] = raw_input().split()
    if  (a == "enter"):
        if ((c + int(n)) > L):
            hold += 1
        else:
            c += int(n)
    else:
        c -= int(n)

print(hold)