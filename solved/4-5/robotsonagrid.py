import collections
input = raw_input
N = int(input())
MOD = 2**31 - 1
arr = []
for _ in range(N):
  line = input()
  arr.append([x=='.' for x in line])
dp = [[0]*N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
  for j in range(N):
    if not arr[i][j] or i==j==0:
      continue
    dp[i][j] = \
      (dp[i-1][j] if i!=0 else 0) + \
      (dp[i][j-1] if j!=0 else 0) % MOD

def poss():
  visited = [[False]*N for _ in range(N)]
  q = collections.deque()
  q.append((0,0))
  while len(q) > 0:
    r,c = q.popleft()
    if r == c == N-1: return True
    if r+1 < N and not visited[r+1][c] and arr[r+1][c]:
      q.append((r+1,c))
      visited[r+1][c] = True
    if r-1 >= 0 and not visited[r-1][c] and arr[r-1][c]:
      q.append((r-1,c))
      visited[r-1][c] = True
    if c+1 < N and not visited[r][c+1] and arr[r][c+1]:
      q.append((r,c+1))
      visited[r][c+1] = True
    if c-1 >= 0 and not visited[r][c-1] and arr[r][c-1]:
      q.append((r,c-1))
      visited[r][c-1] = True
  else:
    return False


if dp[-1][-1] == 0:
  if poss():
    print('THE GAME IS A LIE')
  else:
    print('INCONCEIVABLE')
else:
  print(dp[-1][-1] % MOD)
