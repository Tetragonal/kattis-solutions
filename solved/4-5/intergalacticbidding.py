import math

N,S = [int(x) for x in input().split()]


arr = [input().split() for _ in range(N)]
for i in range(len(arr)): arr[i][1] = int(arr[i][1])
arr = sorted(arr, key=lambda x: x[1], reverse=True)

ans = []

for name, bid in arr:
  if S >= bid:
    S -= bid
    ans.append(name)
if S != 0:
  print(0)
else:
  print(len(ans))
  print('\n'.join(ans))

