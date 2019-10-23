import heapq
import collections

class Node:
  def __init__(self,v):
    self.children = []
    self.id = v

C, L = [int(x) for x in input().split()]

d = dict()
for i in range(C):
  d[i] = Node(i)

adj = dict()

is_child = [False]*C
for x in range(L):
  v1, v2 = [int(x) for x in input().split()]
  if v1 not in adj:
    adj[v1] = []
  if v2 not in adj:
    adj[v2] = []
  adj[v1].append(v2)
  adj[v2].append(v1)

visited = set()
for i in range(C):
  if not is_child[i]:
    root = d[i]
    q = collections.deque()
    q.append(root)
    visited.add(i)
    while len(q) > 0:
      curr = q.popleft()
      if curr.id in adj:
        for x in adj[curr.id]:
          if x in visited: continue
          visited.add(x)
          curr.children.append(d[x])
          is_child[x] = True
          q.append(d[x])

def maxpath(root):
  if len(root.children) == 0:
    return (0, 1)
  best = depth = depth2 = 0
  for x in root.children:
    path,currdepth = maxpath(x)
    if currdepth > depth:
      depth2 = depth
      depth = currdepth
    elif currdepth > depth2:
      depth2 = currdepth
    best = max(best, path, depth+depth2)
  return best, depth+1

max_maxpath = 0
l = []
for i in range(C):
  if not is_child[i]:
    a, _ = maxpath(d[i])
    max_maxpath = max(max_maxpath, a)
    l.append((a+1)//2)
l = sorted(l)

if len(l) == 0: print(0)
elif len(l) == 1:
  print(max_maxpath)
else:
  print(max(max_maxpath,l[-2]+l[-1]+1, l[-3]+l[-2]+2 if len(l)>=3 else 0))
