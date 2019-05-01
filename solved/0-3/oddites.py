N = int(input())
for _ in range(N):
  x = int(input())
  if abs(x) % 2 == 0: print('%d is even' % x)
  else: print('%d is odd' % x)
