input_str = raw_input()
whitespace = 0
lower = 0
upper = 0
symbols = 0
for c in input_str:
    if (c == "_"):
        whitespace += 1
    elif (c.islower()):
        lower += 1
    elif (c.isupper()):
        upper += 1
    else:
        symbols += 1

print(float(whitespace)/float(len(input_str)))
print(float(lower)/float(len(input_str)))
print(float(upper)/float(len(input_str)))
print(float(symbols)/float(len(input_str)))
