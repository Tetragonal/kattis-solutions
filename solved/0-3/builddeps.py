from collections import deque

N = int(raw_input())

g = dict()

for _ in range(N):
  line = raw_input().split()
  dest = line[0][:-1]
  sources = line[1:]
  if dest not in g: g[dest] = []
  for s in sources:
    if s not in g: g[s] = []
    g[s].append(dest)

first = raw_input()
uniq = set([first])
q = deque([first])
while len(q) > 0:
  curr = q.popleft()
  for dest in g[curr]:
    if dest in uniq: continue
    q.append(dest)
    uniq.add(dest)

g = {k:filter(lambda x: x in uniq, v) for k,v in g.items() if k in uniq}
incoming = dict()
for k in g.keys():
  for v in g[k]:
    if v not in incoming: incoming[v] = 0
    incoming[v] += 1

L = []
S = set([first])
ans = []
while len(S) > 0:
  n = S.pop()
  L.append(n)
  for m in g[n]:
    incoming[m] -= 1
    if incoming[m] == 0:
      S.add(m)

print('\n'.join(L))