"""
score[i][j] stores the min score for elements i to j inclusive.

dp[n][k] stores the best result of the first n+1 integers with
  exactly k+1 subsets remaining
dp[n][k] = {
  INF if k > n, because impossible to get k subsets
  0 if k == n, because each integer is its own subset
  score[0][n] if k == 0, because single subset
  min(dp[i][k-1] + score[i][n]) for each i from 0 to n, if k < n
}

return dp[N-1][K-1]
"""
import heapq
import math

class MedianList:
  def __init__(self):
    self.heapleft = []
    self.heapright = []
    self.median = None
    self.score = 0
  def add(self, n):
    if self.median is None:
      self.median = n
    else:
        if n > self.median:
          if len(self.heapright) - len(self.heapleft) > 0:
            heapq.heappush(self.heapleft, -self.median)
            if n > self.heapright[0]:
              self.median = heapq.heappop(self.heapright)
              heapq.heappush(self.heapright, n)
            else:
              self.median = n
          else:
            heapq.heappush(self.heapright, n)
        else:
          if len(self.heapleft) - len(self.heapright) > 0:
            heapq.heappush(self.heapright, self.median)
            if -n > self.heapleft[0]:
              self.median = -heapq.heappop(self.heapleft)
              heapq.heappush(self.heapleft, -n)
            else:
              self.median = n
          else:
            heapq.heappush(self.heapleft, -n)
        self.score += abs(self.median - n)


N,K = [int(x) for x in raw_input().split()]

arr = [int(raw_input()) for _ in range(N)]

INF = 9999999999999
dp = [[INF]*K for _ in range(N)]

score = [[None]*N for _ in range(N)]

# score
for i in range(N):
  l = MedianList()
  for j in range(i,N):
    l.add(arr[j])
    score[i][j] = l.score

# dp base cases
for k in range(K):
  dp[k][k] = 0

# dp cases
for n in range(N):
  dp[n][0] = score[0][n]
  for k in range(1,min(K,n)):
    dp[n][k] = min([dp[i][k-1] + (score[i+1][n] if i+1<=n else 0) for i in range(n+1)])

print(dp[N-1][K-1])
