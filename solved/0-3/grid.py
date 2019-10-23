import collections
N, M = [int(x) for x in input().split()]
arr = []
for _ in range(N):
  arr.append([int(x) for x in input()])

q = collections.deque()
q.append(((0,0,0)))
visited = set()
ans = -1
while len(q) > 0:
  r,c,dist = q.popleft()
  jmp = arr[r][c]
  if r == N-1 and c == M-1:
    ans = dist
    break
  if r+jmp < N and (r+jmp,c) not in visited:
    q.append((r+jmp,c,dist+1))
    visited.add((r+jmp,c))
  if r-jmp >= 0 and (r-jmp,c) not in visited:
    q.append((r-jmp,c,dist+1))
    visited.add((r-jmp,c))
  if c+jmp < M and (r,c+jmp) not in visited:
    q.append((r,c+jmp,dist+1))
    visited.add((r,c+jmp))
  if c-jmp >= 0 and (r,c-jmp) not in visited:
    q.append((r,c-jmp,dist+1))
    visited.add((r,c-jmp))
print(ans)
