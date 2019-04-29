MOD = 1000000007
n, w = input().split()
n = int(n)

meaning = dict()
for _ in range(n):
  word, num = input().split()
  meaning[word] = int(num)

dp = [1] + ([0] * len(w))

for i in range(1,len(w)+1):
  ways = 0
  for k,v in meaning.items():
    if len(k) > i: continue
    elif w[i-len(k):i] == k:
      ways += dp[i-len(k)]*v
  dp[i] = ways
print(dp[-1] % MOD)