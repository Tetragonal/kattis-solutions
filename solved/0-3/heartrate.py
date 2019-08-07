N = int(input())

for _ in range(N):
  b, p = [float(x) for x in input().split()]
  print((b-1)/p*60, b/p*60, (b+1)/p*60)
