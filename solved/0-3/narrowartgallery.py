import sys
INF = -99999999
while True:
  N, K = [int(x) for x in input().split()]
  if N == K == 0: sys.exit()
  v = [list(map(int, input().split())) for _ in range(N)]
  dp = [[[INF,INF,INF] for _ in range(K+1)] for _ in range(N)]
  #print(dp)
  dp[0] = [[sum(v[0]), v[0][1], v[0][0]]] + \
          [[INF, v[0][1], v[0][0]]]+ \
           [[INF,INF,INF] for _ in range(K-1)]
  #print(dp)
  for i in range(1,N):
    for j in range(K+1):
      dp[i][j][0] = max(dp[i-1][j]) + v[i][0] + v[i][1]
      dp[i][j][1] = max(dp[i-1][max(0,j-1)][0], dp[i-1][max(0,j-1)][1]) + v[i][1]
      dp[i][j][2] = max(dp[i-1][max(0,j-1)][0], dp[i-1][max(0,j-1)][2]) + v[i][0]
  #print(sum(map(sum, v)))
  #print(dp)
  print(max(0, max(dp[-1][-1])))