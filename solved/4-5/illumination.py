import sys
sys.setrecursionlimit(int(1e9))
range = xrange
n = 0
g = []
gt = []
used = []
order = []
comp = []
def dfs1(v):
  used[v] = True
  for u in g[v]:
    if not used[u]:
      dfs1(u)
  order.append(v)
def dfs2(v, cl):
  comp[v] = cl
  for u in gt[v]:
    if comp[u] == -1:
      dfs2(u, cl)
def solve_2SAT():
  global used, comp
  used = [False]*n
  for i in range(n):
    if not used[i]:
      dfs1(i)
  
  comp = [-1]*n
  j = 0
  for i in range(n):
    v = order[n-i-1]
    if comp[v] == -1:
      dfs2(v, j)
      j += 1

  return not any(comp[i] == comp[i+1] for i in range(0,n,2))
def true(x):
  return 2*x
def false(x):
  return 2*x+1
def implies(i,j):
  g[i].append(j)
  gt[j].append(i)
def clause(i,j, neg_i, neg_j):
  f1, f2 = (true, false) if neg_i else (false, true)
  f3, f4 = (true, false) if neg_j else (false, true)
  implies(f1(i), f4(j))
  implies(f3(j), f2(i))
def is_true(i):
  implies(false(i), true(i))
def is_false(i):
  implies(true(i), false(i))

import sys
import io
sys.stdin = io.BytesIO(sys.stdin.read())
input = (s.rstrip() for s in sys.stdin).next

N,R,K = map(int, input().split())
lamps = [[int(x)-1 for x in input().split()] for _ in range(K)]

n = 2*K
g = [[] for _ in range(n)]
gt = [[] for _ in range(n)]

# True: vertical
# False: horizontal
for i in range(K):
  for j in range(i+1,K):
    r1, c1 = lamps[i]
    r2, c2 = lamps[j]
    if c1 == c2 and abs(r2 - r1) <= 2*R:
      clause(i,j,False,False)
    elif r1 == r2 and abs(c2 - c1) <= 2*R:
      clause(i,j,True,True)
print(1 if K==1 or solve_2SAT() else 0)
