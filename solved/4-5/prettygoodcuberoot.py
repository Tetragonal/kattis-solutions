import sys
BIG = int("1"+"0"*(500//3+5))

for n in map(int, sys.stdin):
  l = 0
  r = BIG
  while l < r:
    mid = (l+r)//2
    if mid*mid*mid < n:
      l = mid+1
    else:
      r = mid

  if abs(l*l*l-n) < abs((l-1)*(l-1)*(l-1)-n):
    print(l)
  else:
    print(l-1)
  


