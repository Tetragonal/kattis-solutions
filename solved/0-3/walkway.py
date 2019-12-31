import sys
import io
sys.stdin = io.BytesIO(sys.stdin.read())
input = (s.rstrip() for s in sys.stdin).next

import heapq

while True:
  N = int(input())
  if N == 0:
    break
  g = [[] for _ in range(1001)]
  for _ in range(N):
    a,b,h = map(int, input().split())
    g[a].append((b,h))
    g[b].append((a,h))

  start, end = map(int, input().split())
  q = [(0, start)]
  visited = set()
  while len(q):
    dist, curr = heapq.heappop(q)
    if curr in visited:
      continue
    visited.add(curr)
    if curr == end:
      print('%0.2f' % (dist*0.02))
      break
    for (b,h) in g[curr]:
      heapq.heappush(q, (dist+((curr+b)/2.*h), b))
