L, X = [int(x) for x in input().split()]

cnt = 0
curr = 0
for _ in range(X):
  s, n = input().split()
  n = int(n)
  if s == 'leave':
    curr -= n
  elif s == 'enter':
    if n+curr > L:
      cnt += 1
    else: curr += n
print(cnt)
