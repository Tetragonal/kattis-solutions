import sys
from math import sqrt

lines = [x for x in sys.stdin]

def to_range(x_r, w):
  x, r = [int(x) for x in x_r.split()]
  tmp = r**2 - (0.5*w)**2
  if tmp < 0: return 0, 0
  d = sqrt(tmp)
  return (x-d, x+d)

i = 0
while i < len(lines):
  N, L, W = [int(x) for x in lines[i].split()]
  sprinklers = sorted(map(lambda x: to_range(x,W), lines[i+1:i+1+N]), key=lambda x: x[0])

  used = 0
  reach = 0
  j = 0
  best = 0
  while True:
    while j < len(sprinklers) and sprinklers[j][0] < reach and reach < L:
      best = max(best, sprinklers[j][1])
      j += 1
    if best <= reach or reach >= L: break
    else:
      used += 1
      reach = best
  print(used if reach >= L else -1)
  i += N + 1