input = raw_input

N = int(input())
SIZE = N+5
nums = [int(x) for x in input().split()]

A = [0]*SIZE
B = [0]*SIZE
def add(arr,p,v):
  p += 2
  while p < SIZE:
    arr[p] += v
    p += p & -p
def query(arr,p):
  tot = 0
  p += 2
  while p > 0:
    tot += arr[p]
    p -= p & -p
  return tot

d = dict()

for i,x in enumerate(nums):
  if x not in d: d[x] = []
  d[x].append(i)
for i,x in enumerate(nums):
  add(A,i+1,1)

tot = 0
order = sorted(d.items(), key=lambda x: x[0])
for num, indices in order:
  for i in indices:
    add(A,i+1, -1)
  for i in indices:
    tot += query(A,i+1) * query(B,N-i)
  for i in indices:
    add(B,N-i, 1)
print(tot)
