N = int(input())
tot = 0
for _ in range(N):
  qual, year = [float(x) for x in input().split()]
  tot += qual*year
print(tot)
