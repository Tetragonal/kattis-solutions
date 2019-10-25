import collections
import bisect

input = raw_input
N,M,D = [int(x) for x in input().split()]

adj = dict()
inc = dict()
def toposort():
  order = []
  q = collections.deque()
  for k,v in inc.items():
    if v == 0: q.append(k)
  while q:
    curr = q.popleft()
    order.append(curr)
    for v in adj[curr]:
      if inc[v] >= 1:
        inc[v] -= 1
        if inc[v] == 0:
          q.append(v)
  return order

for _ in range(M):
  a,b = [int(x) for x in input().split()]
  if a not in adj:
    adj[a] = set()
    inc[a] = 0
  if b not in adj: 
    adj[b] = set()
    inc[b] = 0
  if b not in adj[a]:
    adj[a].add(b)
    inc[b] += 1
correct = toposort()
orig = [int(input()) for _ in range(N)]

to_i = {x:i for i,x in enumerate(correct)}
valid_num = set(correct)

# Remove non-LIS from list
changes = len(orig)
orig = [to_i[x] for x in orig if x in valid_num]
def lis(nums):
  if len(nums) == 0: return 0
  dp = [nums[0]]
  for x in nums[1:]:
    i = bisect.bisect_left(dp, x)          
    if i == len(dp):
      dp.append(x)
    else:
      dp[i] = x
  return len(dp)
changes -= lis(orig)

# Add missing elements to list
changes += (len(correct)-lis(orig))

print(changes)




