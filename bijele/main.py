valid_set = [1,1,2,2,2,8]
pieces = list(map(int, input().split()))
diff = []
for i in range(len(valid_set)):
    diff.append(valid_set[i] - pieces[i])
print(" ".join(list(map(str, diff))))