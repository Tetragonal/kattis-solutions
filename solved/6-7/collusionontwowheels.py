import collections

def dist(x1, x2, y1, y2):
  return abs(x1-x2) + abs(y1-y2)

N = int(input())
coords = [tuple([int(x) for x in input().split()]) for _ in range(N)]

dists = [[None]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i == j: continue
    x1 = coords[i][0]
    x2 = coords[j][0]
    y1 = coords[i][1]
    y2 = coords[j][1]
    dists[i][j] = dist(x1, x2, y1, y2)

def p(n):
  color = [None]*N
  def bipartite(x):
    color[x] = 1
    q = collections.deque()
    q.append(x)
    while len(q) > 0:
      curr = q.pop()
      for i in range(N):
        if curr == i: continue
        if dists[curr][i] > n:
          if color[i] is None:
            color[i] = 1-color[curr]
            q.append(i)
          elif color[i] == color[curr]:
            return False
    return True

  for i in range(N):
    if color[i] is None:
      if not bipartite(i):
        return False
  return True

l = 0
r = 10005
while l < r:
  mid = (l+r)//2
  if not p(mid):
    l = mid+1
  else:
    r = mid
print(l)
