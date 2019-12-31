import sys
import io
sys.stdin = io.BytesIO(sys.stdin.read())
input = (s.rstrip() for s in sys.stdin).next

M,N = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Whether we can make every child not exceed x
def p(x):
  return sum(max(0,a-x) for a in arr) <= M

l = 0
r = max(arr)
while l < r:
  mid = (l+r)//2
  if not p(mid):
    l = mid + 1
  else:
    r = mid
leftover = M - sum(max(0,a-l) for a in arr)
arr = sorted([min(a, l) for a in arr])
for i in range(leftover):
  arr[-i-1] -= 1
print(sum(x*x for x in arr))
