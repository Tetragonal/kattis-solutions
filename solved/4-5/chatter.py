import sys
import collections
for line in sys.stdin:
  parent = dict()
  size = dict()
  def make_set(vertice):
    parent[vertice] = vertice
    size[vertice] = 1
  def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
  def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
      if size[root1] > size[root2]:
        parent[root2] = root1
        size[root1] += size[root2]
        size[root2] = 0
      else:
        parent[root1] = root2
        size[root2] += size[root1]
        size[root1] = 0

  n, r, a, b, c = [int(x) for x in line.split()]
  for i in range(n): make_set(i)
  for _ in range(n):
    x = y = -1
    while x == y:
      r = (r * a + b) % c
      x = r % n
      r = (r * a + b) % c
      y = r % n
    union(x,y)
  cnt = collections.Counter()
  tot = 0
  for _,v in size.items():
    if v == 0: continue
    cnt[v] += 1
    tot += 1
  
  ans = str(tot)
  for k,v in sorted(cnt.items(), key=lambda x: x[0], reverse=True):
    ans += " "
    if v == 1: ans += str(k)
    else: ans += "%dx%d" % (k,v)
  print(ans)
