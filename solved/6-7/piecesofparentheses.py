n = int(raw_input())


def parse(s):
    maxneg = 0
    maxnegi = 0
    count = 0
    for i, c in enumerate(s):
        if c == '(':
            count += 1
        else:
            count -= 1
            if count <= maxneg:
                maxneg = count
                maxnegi = i
    poscount = 0
    for c in s[maxnegi+1:]:
        if c == '(': poscount += 1
        else: poscount -= 1
    return maxneg, count, len(s), s, poscount


parsed = [parse(raw_input()) for _ in range(n)]


# sort positive count strings descending from maxneg (first consider all strings with 0 maxneg)
a = filter(lambda x: x[1] >= 0, parsed)
a = sorted(a, key=lambda x: x[0], reverse=True)

# sort negative count strings descending from maxpos (first consider all strings with highest maxpos)
b = filter(lambda x: x[1] < 0, parsed)
b = sorted(b, key=lambda x: x[4], reverse=True)


parsed = a + b
#print(parsed)

dp = [0] * (n*301)

# i = the ith string
# j = the max length of a string with this much count
dp[parsed[0][1]] = parsed[0][2] if parsed[0][0] == 0 else 0
#print(parsed[0][3] + '\t\t', dp)
for maxneg, count, length, s, _ in parsed[1:]:
    dp_new = [0] * (n*301)
    if maxneg == 0:
        dp_new[count] = max(dp[count], length)
    for i in range(len(dp)):
        if i - count < 0 or i - count >= len(dp) or dp[i - count] == 0 or count-maxneg > i:
            dp_new[i] = max(dp_new[i], dp[i])
        # if maxneg < 0 and abs(maxneg) > i: continue
        else:
            dp_new[i] = max(dp_new[i], dp[i], dp[i - count] + length)
    #print(s + '\t\t', dp_new)
    dp = dp_new
print(dp[0])
