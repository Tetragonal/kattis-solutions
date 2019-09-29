N = int(raw_input())
s = raw_input()

nums = []
symbols = []
for i,x in enumerate(s.split()):
  if i % 2 == 0: nums.append(int(x))
  else: symbols.append(x)

INF = 9999999
maxes = [[None]*N for _ in range(N)]
mins = [[None]*N for _ in range(N)]

"""
mins/maxes[i][j] stores the max and min starting at i and ending at j.
Base:
  mins[i][i] = maxes[i][i] nums[i], because no operators
  mins[i][j] = min(mins[i][k] <symbols[k]> mins[k][j] for i<=k<=j)
"""
for i in range(N):
  mins[i][i] = maxes[i][i] = nums[i]
for i in range(1,N):
  for j in range(N):
    mins[j][(j+i)%N] = INF
    maxes[j][(j+i)%N] = -INF
    for k in range(i):
      curr = symbols[(j+k)%N]
      if curr == '*' or curr == '?':
        a = mins[j][(j+k)%N] * mins[(j+k+1)%N][(j+i)%N]
        b = mins[j][(j+k)%N] * maxes[(j+k+1)%N][(j+i)%N]
        c = maxes[j][(j+k)%N] * mins[(j+k+1)%N][(j+i)%N]
        d = maxes[j][(j+k)%N] * maxes[(j+k+1)%N][(j+i)%N]
        mins[j][(j+i)%N] = min(mins[j][(j+i)%N], a,b,c,d)
        maxes[j][(j+i)%N] = max(maxes[j][(j+i)%N], a,b,c,d)
      if curr == '+' or curr == '?':
        mins[j][(j+i)%N] = min(mins[j][(j+i)%N], mins[j][(j+k)%N] + mins[(j+k+1)%N][(j+i)%N])
        maxes[j][(j+i)%N] = max(maxes[j][(j+i)%N], maxes[j][(j+k)%N] + maxes[(j+k+1)%N][(j+i)%N])
      if curr == '-' or curr == '?':
        mins[j][(j+i)%N] = min(mins[j][(j+i)%N], mins[j][(j+k)%N] - maxes[(j+k+1)%N][(j+i)%N])
        maxes[j][(j+i)%N] = max(maxes[j][(j+i)%N], maxes[j][(j+k)%N] - mins[(j+k+1)%N][(j+i)%N])

print(''.join(str(abs(mins[i][(N-1+i)%N])) + str(abs(maxes[i][(N-1+i)%N])) for i in range(N)))
