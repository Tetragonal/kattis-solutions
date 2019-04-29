from collections import deque

MAX_DIST = 1000

def dist(s1, s2):
  x1, y1 = [int(x) for x in s1.split()]
  x2, y2 = [int(x) for x in s2.split()]
  return abs(x1-x2) + abs(y1-y2)

T = int(input())

for _ in range(T):
  N = int(input())
  adj = dict()

  start = input()
  stores = [input() for _ in range(N)]
  destination = input()
  nodes = [start] + [destination] + stores 

  for n in nodes:
    conn = []
    for n2 in nodes:
      if n == n2: continue
      if dist(n, n2) <= MAX_DIST:
        conn.append(n2)
    adj[n] = conn
  
  q = deque()
  q.append(start)
  visited = set()
  happy = False
  while len(q) > 0 and not happy:
    curr = q.popleft()
    for node in adj[curr]:
      if node in visited: continue
      elif node == destination:
        happy = True
        break
      else:
        q.append(node)
        visited.add(node)

  print('happy' if happy else 'sad')
 
