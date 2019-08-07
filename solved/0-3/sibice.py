import math
N,W,H = [int(x) for x in input().split()]

hypotenuse = math.sqrt(W*W + H*H)

for _ in range(N):
  n = int(input())
  if hypotenuse >= n: print('DA')
  else: print('NE')
