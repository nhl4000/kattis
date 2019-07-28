max_score = -1
winner = -1
for i in range(1, 5 + 1):
    scores_temp = list(map(int, raw_input().split()))
    if (sum(scores_temp) > max_score):
        max_score = sum(scores_temp)
        winner = i
print("%d %d" % (winner, max_score))