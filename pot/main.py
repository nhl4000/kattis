n = int(raw_input())
s = 0
for _ in range(n):
    num = raw_input()
    power = num[-1]
    number = num[:-1]
    s += (int(number)**int(power))
print(s)
