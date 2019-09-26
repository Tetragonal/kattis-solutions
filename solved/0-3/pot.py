N = int(input())
tot = 0
for _ in range(N):
  x = input()
  base, exp = x[:-1], x[-1]
  tot += int(base) ** int(exp)
print(tot)
