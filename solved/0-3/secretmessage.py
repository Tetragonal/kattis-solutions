import math
n = int(input())
for _ in range(n):
  line = input()
  m = math.ceil(math.sqrt(len(line)))
  line += "*" * (m**2 - len(line))
  arr = [[x for x in line[i:i+m]] for i in range(0, m*m, m)]
  ans = ""
  for c in range(m):
    for r in range(m-1,-1,-1): 
      ans += arr[r][c]
  print(ans.replace('*', ''))
