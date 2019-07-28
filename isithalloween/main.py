[month, day] = raw_input().split()

if (int(day) == 31) and (month == "OCT"):
    print("yup")
elif (int(day) == 25) and (month == "DEC"):
    print("yup")
else:
    print("nope")