[n, b] = raw_input().split()
n = int(n)
s = 0
for _ in range(4*n):
    hand = raw_input()
    if (hand[1] == b):
        # dominant
        if (hand[0] == "7"):
            s += 0
        elif (hand[0] == "8"):
            s += 0
        elif (hand[0] == "9"):
            s += 14
        elif (hand[0] == "T"):
            s += 10
        elif (hand[0] == "J"):
            s += 20
        elif (hand[0] == "Q"):
            s += 3
        elif (hand[0] == "K"):
            s += 4
        elif (hand[0] == "A"):
            s += 11
    else:
        # non-dominant
        if (hand[0] == "7"):
            s += 0
        elif (hand[0] == "8"):
            s += 0
        elif (hand[0] == "9"):
            s += 0
        elif (hand[0] == "T"):
            s += 10
        elif (hand[0] == "J"):
            s += 2
        elif (hand[0] == "Q"):
            s += 3
        elif (hand[0] == "K"):
            s += 4
        elif (hand[0] == "A"):
            s += 11
print(s)