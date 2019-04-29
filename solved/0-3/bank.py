from queue import PriorityQueue
from functools import cmp_to_key

def cmp(x, y):
  if x[0] == y[0]:
    return x[1] - y[1]
  else: return y[0] - x[0]

N, T = [int(x) for x in input().split()]

arr = set()
for _ in range(N):
  a, b = [int(x) for x in input().split()]
  arr.add((a,b))
#print(arr)
time = T

tot = 0
while time >= 0:
  valid = list(filter(lambda x: x[1] >= time, arr))
  valid = sorted(valid, key=cmp_to_key(cmp))
  #print(valid)
  if len(valid) > 0:
    tot += valid[0][0]
    #print(valid[0])
    arr.remove(valid[0])
  time -= 1

print(tot)
#print('unused:', arr)