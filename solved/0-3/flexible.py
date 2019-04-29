w, n = [int(x) for x in input().split()]
ints = [0] + [int(x) for x in input().split()] + [w]

ans = set()
for i in ints:
  for j in ints:
    if j > i: ans.add(j-i)
print(' '.join([str(x) for x in sorted(ans)]))	

