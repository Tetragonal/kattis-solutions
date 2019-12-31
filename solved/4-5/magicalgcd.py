import sys
import io
sys.stdin = io.BytesIO(sys.stdin.read())
input = (s.rstrip() for s in sys.stdin).next

from fractions import gcd

T = int(input())
for _ in range(T):
  N = int(input())
  arr = [int(x) for x in input().split()]

  best = 0
  gcds = []
  for i,x in enumerate(arr):
    for j,(i2,x2) in enumerate(gcds):
      gcds[j] = (i2, gcd(x2,x))
      best = max(best, (i-i2+1)*gcds[j][1])
    gcds = [y for j,y in enumerate(gcds) if j==0 or gcds[j][1] > gcds[j-1][1]]
    gcds.append((i, x))
    best = max(best, x)
  print(best)
