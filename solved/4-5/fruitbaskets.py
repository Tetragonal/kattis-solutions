from itertools import combinations

N = int(input())
nums = list(map(int, input().split()))
total = (2 ** N) * sum(nums) // 2

for size in range(5):
  for s in combinations(nums, size):
    if sum(s) < 200:
      total -= sum(s)
print(total)