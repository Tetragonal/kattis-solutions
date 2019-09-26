import sys

while True:
  cans = [int(x) for x in raw_input().split()[1:]]
  if cans == []: sys.exit(0)

  if len(cans) == 1: 
    print('%d 0' % sum(cans))
    continue

  tot = sum(cans)
  size = max(tot, max(cans)*2)

  dp = [False] * (size//2+5)

  for c in cans:
    dp2 = [x for x in dp]
    dp2[c] = True
    for i in range(c, size//2+5):
      if dp[i-c]: dp2[i] = True
    dp = dp2

  
  for i in range(tot//2):
    if dp[tot//2 - i]:
      a = tot//2-i
      b = tot - a
      print('%d %d' % (max(a,b), min(a,b)))
      break
