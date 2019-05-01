X = int(input())
N = int(input())

total = X*(N+1)
for _ in range(N):
  total -= int(input())
print(total)
