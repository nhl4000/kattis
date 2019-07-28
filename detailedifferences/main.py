ans = []
n = int(raw_input())
for _ in range(n):
    line1 = raw_input()
    line2 = raw_input()
    line3 = ""
    for i in range(len(line1)):
        if (line1[i] == line2[i]):
            line3 += "."
        else: 
            line3 += "*"
    ans.append(line1)
    ans.append(line2)
    ans.append(line3)
    ans.append(" ")


for i in ans:
    print(i)