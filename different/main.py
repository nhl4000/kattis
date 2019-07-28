diff = []
while (True):
    try:
        [a,b] = list(map(int, raw_input().split()))
        diff.append(abs(a-b))
    except:
        break
print("\n".join(list(map(str, diff))))
    