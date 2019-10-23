import collections
N = int(input())

d = dict()
input_order = []
for _ in range(N):
  arr = [int(x) for x in input().split()]
  d[arr[0]] = arr[2:]
  input_order.append(arr[0])

q = collections.deque()
q.append(0)
visited = set([0])
while len(q) > 0:
  curr = q.popleft()
  for x in d[curr]:
    if x in visited: continue
    q.append(x)
    visited.add(x)

trapped = set(input_order)
trapped.remove(0)
for x in input_order:
  if x == 0: continue
  q = collections.deque()
  q.append(x)
  visited_rev = set([x])
  while len(q) > 0:
    curr = q.popleft()
    if curr == 0:
      trapped.remove(x)
      break
    for e in d[curr]:
      if e in visited_rev: continue
      q.append(e)
      visited_rev.add(e)

ans_unreach = []
ans_trapped = []
for x in input_order:
  if x not in visited:
    ans_unreach.append(x)
  if x in trapped:
    ans_trapped.append(x)
for x in ans_trapped:
  print('TRAPPED %d' % x)
for x in ans_unreach:
  print('UNREACHABLE %d' % x)
if len(ans_trapped) == len(ans_unreach) == 0:
  print('NO PROBLEMS')

