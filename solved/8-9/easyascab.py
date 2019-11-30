import collections
import sys
input = raw_input
L, N = input().split()
N = int(N)
L = ord(L) - ord('a')

def toposort(adj, inc):
  order = []
  q = collections.deque()
  for i,x in enumerate(inc):
    if x == 0: q.append(i)
  while q:
    curr = q.popleft()
    order.append(curr)
    for v in adj[curr]:
      if inc[v] >= 1:
        inc[v] -= 1
        if inc[v] == 0:
          q.append(v)
  return order

def get_edge(s1, s2):
  for x,y in zip(s1, s2):
    if x != y:
      return (x,y)
  if len(s2) < len(s1):
    print('IMPOSSIBLE')
    sys.exit(0)
  return None

edges = set()
adj = [[] for _ in range(L+1)]
inc = [0]*(L+1)
strs = [input() for _ in range(N)]
for i in range(len(strs)-1):
  j = i+1
  edge = get_edge(strs[i], strs[j])
  if edge is not None:
    edges.add(edge)

for x,y in edges:
  x = ord(x) - ord('a')
  y = ord(y) - ord('a')
  adj[x].append(y)
  inc[y] += 1

order = toposort(adj, inc)
to_idx = {x:i for i,x in enumerate(order)}
if len(order) < L+1:
  print('IMPOSSIBLE')
  sys.exit(0)

for i in range(L+1):
  for j in adj[i]:
    if to_idx[i] > to_idx[j]:
      print('IMPOSSIBLE')
      sys.exit(0)

for i in range(L):
  if order[i+1] not in adj[order[i]]:
    print('AMBIGUOUS')
    sys.exit(0)

print(''.join([chr(x+ord('a')) for x in order]))
