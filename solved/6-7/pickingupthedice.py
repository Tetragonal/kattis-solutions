K,T = [int(x) for x in input().split()]
dice = [int(x) for x in input().split()]

"""
dp[i][j][k]: can you sum up to j using k of the first i numbers
"""

dp = [[[False]*(K+1) for _ in range(6*(K+1))] for _ in range(K+1)]

dp[0][0][0] = True

for i in range(1,K+1):
  for j in range(6*(K+1)):
    for k in range(i+1):
      dp[i][j][k] = dp[i-1][j][k] or dp[i-1][j-dice[i-1]][k-1]


"""
dp2[i][j] = number of ways to roll j by rolling i dice
"""
dp2 = [[0]*(6*(K+1)) for _ in range(K+1)]
dp2[0][0] = 1
for i in range(1,K+1):
  for j in range(6*(K+1)):
    dp2[i][j] = sum([0] + [dp2[i-1][j-x] for x in range(1,7) if j-x >= 0])

"""
dp[-1][i][j]: can you sum up to i using j numbers
dp2[j][target] = number of ways to roll target by rolling j dice

for each i we can sum up to using j numbers:
  target = T - (sum(dice)-i)
  prob = dp2[j][target] / (6**j)

ans = index of best prob
"""
tot = sum(dice)
best = -float('inf')
best_i = 0
for i in range(6*(K+1)):
  for j in range(K+1):
    if dp[-1][i][j]:
      target = T - (tot - i)
      ans = dp2[j][target]
      denom = (6**j)
      if ans * (6**best_i) > best * denom:
        best = ans
        best_i = j
print(best_i)
