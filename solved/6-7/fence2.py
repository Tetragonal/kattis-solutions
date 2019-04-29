from functools import reduce
from math import ceil

_, N = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

def p(arr, n):
  return reduce(lambda acc,x: acc + int(round(x/n, 5)), arr, 0) < N

EPS = 1e-10
lo = 0.0
hi = 10005.0
while hi - lo > EPS:
  mid = (lo + hi) / 2.0
  if p(arr, mid): hi = mid
  else: lo = mid

lo = round(lo, 5)

print(reduce(lambda acc, x: acc + ceil(x/lo) - 1, arr, 0))