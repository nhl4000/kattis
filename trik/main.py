characters = raw_input()
cup_location = 1
for c in characters:
    if (c == "A"):
        if (cup_location == 1):
            cup_location = 2
        elif (cup_location == 2):
            cup_location = 1
    elif (c == "B"):
        if (cup_location == 2):
            cup_location = 3
        elif (cup_location == 3):
            cup_location = 2
    elif (c == "C"):
        if (cup_location == 1):
            cup_location = 3
        elif (cup_location == 3):
            cup_location = 1
print(cup_location)