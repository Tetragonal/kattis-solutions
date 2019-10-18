N = int(input())

best = 0
arr = [int(x) for x in input().split()]

tot = 0
best = 0
for i,n in enumerate(arr):
  tot += n
  best = max(best, tot/(i+1))

tot = 0
for i,n in enumerate(arr[::-1]):
  tot += n
  best = max(best, tot/(i+1))

print(best)
