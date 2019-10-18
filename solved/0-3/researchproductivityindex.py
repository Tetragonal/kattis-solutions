N = int(input())
probs = sorted([int(x)/100.0 for x in  input().split()], reverse=True)

#print(probs)
# [l:r] inclusive
dp = [[[0]*(N+1) for _ in range(N)] for _ in range(N)]
for i in range(N):
  dp[i][i][1] = probs[i]
 
for i in range(N):
  curr = 1  
  for j in range(i,N):
    curr *= (1-probs[j])
    dp[i][j][0] = curr

for r in range(N):
  for l in range(r-1,-1,-1):
    for k in range(1, N+1):
      dp[l][r][k] = probs[l] * dp[l+1][r][k-1] + (1-probs[l]) * dp[l+1][r][k]

#print(dp)
best = 0
for i in range(N):
#  print(i,[dp[0][i][k] for k in range(N+1)])
#  print(sum([dp[0][i][k] for k in range(N+1)]), 'hi')
  arr = [dp[0][i][k] * k**(k/(i+1)) for k in range(1,N+1)]
  curr = sum(arr)
#  print(curr)
  if curr > best: best = curr
print(best)
