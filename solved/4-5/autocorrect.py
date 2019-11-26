import collections
input = raw_input
N,M = map(int,input().split())
freq = [input() for _ in range(N)]
search = [input() for _ in range(M)]

class MWTNode:
  def __init__(self):
    self.children = dict()
    self.parent = None
    self.complete = None
    self.dist = None
  def insert(self, s):
    curr = self
    for x in s:
      if x not in curr.children:
        curr.children[x] = MWTNode()
        curr.children[x].parent = curr
      curr = curr.children[x]
    curr.autocomplete()

  def autocomplete(self):
    curr = self
    while curr.parent is not None:
      curr.complete = self
      curr = curr.parent
  
  def find(self, s):
    curr = self
    dist = 0
    for i,x in enumerate(s):
      if x not in curr.children: break
      curr = curr.children[x]
      dist = min(dist, curr.dist-i-1)
    return len(s) + dist
  
  # Debug
  def __str__(self):
    if self.parent is None:
      return ''
    return str(self.parent) + self.v 

mwt = MWTNode()
for x in freq[::-1]:
  mwt.insert(x)
mwt.complete = None

q = collections.deque()
q.append((mwt, 0))
mwt.dist = 0
while len(q):
  curr, dist = q.popleft()
  for node in curr.children.values():
    if node.dist is not None: continue
    q.append((node,dist+1))
    node.dist = dist+1
  if curr.parent and curr.parent.dist is None:
    q.append((curr.parent, dist+1))
    curr.parent.dist = dist+1
  if curr.complete and curr.complete.dist is None:
    q.append((curr.complete, dist+1))
    curr.complete.dist = dist+1

for x in search:
  print(mwt.find(x))

