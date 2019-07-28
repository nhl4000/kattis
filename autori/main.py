input_str = raw_input()
uppers = []
for c in input_str:
    if (c.isupper()):
        uppers.append(c)
print("".join(uppers))