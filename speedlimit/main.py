
distances = []
while(True):
    distance = 0
    previous_t = 0
    i = int(raw_input())
    if (i == -1):
        break
    for _ in range(i):
        [s, t] = list(map(int, raw_input().split()))
        distance +=  s * (t -previous_t)
        previous_t = t
    distances.append(str(distance)+" miles")
print("\n".join(distances))