import sys
from math import ceil

def p(arr, n, B):
  cnt = 0
  for e in arr: cnt += ceil(e/n)
  return cnt <= B

while True:
  N, B = [int(x) for x in input().split()]
  if N == -1: sys.exit()

  arr = []
  for _ in range(N):
    arr.append(int(input()))

  lo = 0
  hi = 6000000
  while lo <= hi:
    mid = (lo + hi) // 2
    if p(arr, mid, B): hi = mid-1
    else: lo = mid+1

  input()
  print(lo)