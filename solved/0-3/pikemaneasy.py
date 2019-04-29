MOD = 1000000007

N, T = [int(x) for x in input().split()]
A, B, C, t0 = [int(x) for x in input().split()]

arr = [t0]
for _ in range(N-1):
  arr.append(((A * arr[-1] + B) % C) + 1)

arr = sorted(arr)

penalty = 0
solved = 0
time = 0

for p in arr:
  time += p
  if time > T: break
  else:
    solved += 1
    penalty += time

print(solved, penalty % MOD)