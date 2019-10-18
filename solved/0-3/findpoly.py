import sys
import collections
arr = ''.join(sys.stdin).split(';')[:-1]
adj = dict()
for i in range(len(arr)):
  arr[i] = arr[i].replace(' ', '').replace('\n', '')
  tmp = arr[i].split('),(')
  tmp = (tmp[0] + ')', '(' + tmp[1])
  if tmp[0] not in adj: adj[tmp[0]] = []  
  if tmp[1] not in adj: adj[tmp[1]] = []  
  adj[tmp[0]].append(tmp[1])
  adj[tmp[1]].append(tmp[0])

visited = set()
poly = 0
fig = 0
def bfs(x):
  max_degree = -float('inf')
  min_degree = float('inf')
  size = 0
  visited.add(x)
  q = collections.deque()
  q.append(x)
  while len(q) > 0:
    curr = q.popleft()
    max_degree = max(max_degree, len(adj[curr]))
    min_degree = min(min_degree, len(adj[curr]))
    size += 1
    for e in adj[curr]:
      if e not in visited:
        visited.add(e)
        q.append(e)
  return max_degree == min_degree == 2 and size > 2

for x in adj.keys():
  if x not in visited:
    fig += 1
    if bfs(x):
      poly += 1

print('%d %d' % (fig, poly))

