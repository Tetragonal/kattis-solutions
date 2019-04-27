def fac(n): return fac(n-1)*n if n > 1 else 1
T = int(input())
lines = [int(input()) for _ in range(T)]
print('\n'.join(map(lambda x: str(fac(x) % 10), lines)))
