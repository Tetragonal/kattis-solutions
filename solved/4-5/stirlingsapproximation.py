import math

while True:
  N = int(input())
  if N == 0: break
  a = math.pow(math.e, N*(1 - math.log(N)) + math.lgamma(N+1))
  b = math.sqrt(2*math.pi*N)

  print('{0:.25f}'.format(a/b))
