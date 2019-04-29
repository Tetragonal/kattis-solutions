n, t = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]

c = 0
a = 0
for e in tasks:
  if c + e <= t:
    c += e
    a += 1
  else: break
print(a)
