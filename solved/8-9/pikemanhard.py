import sys
MOD = 1000000007

N, T = [int(x) for x in input().split()]
A, B, C, t0 = [int(x) for x in input().split()]

arr = [t0]
uniq = set([t0])
cycle_start = 0

# by pidgeonhole, eventually will create a cycle if N is large
# 1. anything before the cycle is singleton
# 2. the cycle repeats some number of times
# 3. there will be 1 extra ocurrence of the last uncompleted cycle
for _ in range(N-1):
  ti = ((A * arr[-1] + B) % C) + 1
  if ti in uniq:
    cycle_start = arr.index(ti)
    break
  else:
    arr.append(ti)
    uniq.add(ti)

cycle_length = len(arr) - cycle_start
singletons = set(arr[:cycle_start])
remainder = set(arr[cycle_start:cycle_start+ (N-cycle_start) % cycle_length])
duplicates = (N-cycle_start) // cycle_length

arr = sorted(arr)

penalty = 0
solved = 0
time = T
#print(arr)
for p in arr:
  if p in singletons: occurrences = 1
  else: occurrences = duplicates + (1 if p in remainder else 0)

  num_to_complete = min(time//p, occurrences)
  if num_to_complete == 0: break
  #print(time, num_to_complete)
  penalty += num_to_complete * (T-time) + (num_to_complete*(num_to_complete+1)*p//2)
  solved += num_to_complete
  time -= p * num_to_complete

print(solved, penalty % MOD)