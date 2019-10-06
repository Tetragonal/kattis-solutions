import sys
import collections

ANS_FMT = """Total %d
Unallocated %d
Contested %d
%s
"""

lines = list(sys.stdin)
line_idx = 0
while line_idx < len(lines):
  W,H = [int(x) for x in lines[line_idx].split()]
  N = int(lines[line_idx+1])
  office = [[[] for _ in range(W)] for _ in range(H)]
  employees = lines[line_idx+2:line_idx+2+N]
  line_idx += 2+N
  
  cnt = collections.Counter()
  names = []
  unalloc = 0
  contest = 0
  for employee in employees:
    name, *vals = employee.split()
    names.append(name)
    x1, y1, x2, y2 = map(int, vals)
    for i in range(y1, y2):
      for j in range(x1, x2):
        office[i][j].append(name)
  for i in range(H):
    for j in range(W):
      if len(office[i][j]) > 1: contest += 1
      elif len(office[i][j]) == 0: unalloc += 1
      else:
        cnt[office[i][j][0]] += 1
  print(ANS_FMT % (H*W, unalloc, contest,'\n'.join([x + ' ' + str(cnt[x]) for x in names])))
