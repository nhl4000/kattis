[x, y] = list(map(int, raw_input().split()))
if ((4*x + 3*y) % 2 == 0):
    print("possible")
else:
    print("impossible")