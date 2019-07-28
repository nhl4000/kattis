[g, s, c] = list(map(int, raw_input().split()))

limit = g*3 + s*2 + c

ans = ""
if (limit >= 8):
    ans += "Province"
elif (limit >= 5):
    ans += "Duchy"
elif (limit >= 2):
    ans += "Estate"

if (ans != ""):
    ans += " or "

if (limit >= 6):
    ans += "Gold"
elif (limit >= 3):
    ans += "Silver"
elif (limit >= 0):
    ans += "Copper"

print(ans)