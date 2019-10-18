import math
M, N = [int(x) for x in input().split()]

g = math.gcd(M,N)
# odd odd: 1
# even even: 0
# odd even: 0
#print(M//g, N//g)

print(g * (1 if (M//g)%2==1 and (N//g)%2==1 else 0))
  
