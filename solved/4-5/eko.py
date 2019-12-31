import sys
import io
sys.stdin = io.BytesIO(sys.stdin.read())
input = (s.rstrip() for s in sys.stdin).next

N,M = map(int, input().split())
arr = [int(x) for x in input().split()]

def p(x):
  tot = 0
  for a in arr:
    tot += max(0,a-x)
    if tot >= M:
      return True
  return False

l = 0
r = max(arr)
while l < r:
  mid = (l+r+1)//2
  if p(mid):
    l = mid
  else:
    r = mid-1
print(l)

