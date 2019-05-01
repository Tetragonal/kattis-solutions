N, M = [int(x) for x in input().split()]

arr = [0] * (N+M+5)
for a in range(N):
  for b in range(M):
    arr[a+b+2] += 1

maximum = max(arr)

for i in range(N+M+5):
  if arr[i] == maximum: print(i)
