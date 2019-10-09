N = int(raw_input())
A = [int(x) for x in raw_input().split()] 
dp = [1]
pre = [A[0]]
maxes = [A[0]]
for x in A[1:]:
  pre.append(pre[-1] + x)

for i in range(1,N):
  for j in range(i-1, -1, -1):
    if pre[i] - pre[j] >= maxes[j]:
      maxes.append(pre[i] - pre[j])
      dp.append(dp[j] + 1)
      break
  else: 
    maxes.append(maxes[i-1] + A[i])
    dp.append(dp[i-1])
print(dp[-1])
