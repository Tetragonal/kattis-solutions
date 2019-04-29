from collections import deque

N, M = [int(x) for x in input().split()]

is_sea = [[True for _ in range(M+2)]] + \
[[True] + [True if x=='0' else False for x in input()] + [True] for _ in range(N)] + \
[[True for _ in range(M+2)]]

sea = set()
q = deque([(0,0)])
while not len(q)==0:
  r, c = q.popleft()
  if (r,c) in sea: continue
  sea.add((r,c))
  if r-1>=0 and is_sea[r-1][c]: q.append((r-1, c))
  if r+1<len(is_sea) and is_sea[r+1][c]: q.append((r+1, c))
  if c-1>=0 and is_sea[r][c-1]: q.append((r, c-1))
  if c+1<len(is_sea[0]) and is_sea[r][c+1]: q.append((r, c+1))

coast = 0
for r, c in sea:
  if r-1>=0 and not is_sea[r-1][c]: coast += 1
  if r+1<len(is_sea) and not is_sea[r+1][c]: coast += 1
  if c-1>=0 and not is_sea[r][c-1]: coast += 1
  if c+1<len(is_sea[0]) and not is_sea[r][c+1]: coast += 1
print(coast)