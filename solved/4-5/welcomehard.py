T = int(input())
d = {'w': [0], 'e': [1, 6, 14], 'l': [2], 'c': [3, 11], 'o': [4, 9, 12], 'm': [5, 18], ' ': [7, 10, 15], 't': [8], 'd': [13], 'j': [16], 'a': [17]}
for t in range(T):
  dp = [0] * 19
  s = input()
  for c in s:
    if c not in d: continue
    for i in d[c]:
      if c == 'w': dp[0] += 1
      else: dp[i] = dp[i] + dp[i-1]

  print('Case #%d: %s' % (t+1, str(dp[-1])[-4:].zfill(4)))
