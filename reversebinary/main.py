n = raw_input()
print(int(str(bin(int(n))[2:])[::-1], 2))
