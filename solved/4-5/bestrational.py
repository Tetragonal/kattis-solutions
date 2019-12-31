from fractions import Fraction
T = int(input())
for _ in range(T):
  K,M,X = input().split()
  K = int(K)
  M = int(M)
  X = float(X)
  print(K, Fraction(X).limit_denominator(M))
