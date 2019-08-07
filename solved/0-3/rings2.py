N, M = [int(x) for x in input().split()]

arr = [[] for _ in range(N)]
for i in range(N):
  arr[i] = [x=='T' for x in input()]


INF = 9999999
ans = [[INF]*M for _ in range(N)]

q = []
for r in range(N):
  for c in range(M):
    if not arr[r][c]: ans[r][c] = 0
    elif c==0 or r==0 or c+1==M or r+1==N or (c-1>=0 and not arr[r][c-1]) or (c+1<M and not arr[r][c+1]) or (r-1>=0 and not arr[r-1][c]) or (r+1<N and not arr[r+1][c]):
      ans[r][c] = 1
      q.append((r,c,1))

while len(q) > 0:
  q2 = []
  for r,c,l in q:
    if c-1>=0 and ans[r][c-1] == INF:
      ans[r][c-1] = l+1
      q2.append((r,c-1, l+1))
    if c+1<M and ans[r][c+1] == INF:
      ans[r][c+1] = l+1
      q2.append((r,c+1, l+1))
    if r-1>=0 and ans[r-1][c] == INF:
      ans[r-1][c] = l+1
      q2.append((r-1,c, l+1))
    if r+1<N and ans[r+1][c] == INF:
      ans[r+1][c] = l+1
      q2.append((r+1,c, l+1))
  q = q2

highest = max(max(row) for row in ans)
def fmt(n):
  if highest < 10:
    if n == 0: 
      return '..'
    elif n < 10:
      return '.' + str(n)
    else:
      return str(n)
  else:
    if n == 0:
      return '...'
    elif n < 10:
      return '..' + str(n)
    elif n < 100:
      return '.' + str(n)
    else:
      return str(n)


for row in ans:
  print(''.join(map(fmt, row)))





