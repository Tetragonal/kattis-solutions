import sys

facs = dict()
def fac(n):
  if n not in facs:
    if n <= 1: facs[n] = 1
    else: facs[n] = n * fac(n-1)
  return facs[n]

def ans(arr, k):
  if len(arr) == 0: return []
  x = fac(len(arr)-1)
  return [str(arr[k//x])] + ans(arr[:k//x] + arr[k//x+1:], k % x)

for line in sys.stdin:
  n, k = map(int, line.split())
  print(' '.join(ans(list(range(1, n+1)),k)))
