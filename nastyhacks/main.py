n = int(raw_input())
l = []
for _ in range(n):
    a = list(map(int, raw_input().split()))
    l.append(a)
    
    
for a in l:
    if (a[0] > (a[1]-a[2])):
        print("do not advertise")
    elif (a[0] == (a[1]-a[2])):
        print("does not matter")
    else:
        print("advertise")