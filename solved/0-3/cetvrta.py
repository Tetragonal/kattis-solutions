x = set()
y = set()
for _ in range(3):
  a, b = [int(x) for x in input().split()]
  if a not in x: x.add(a)
  else: x.remove(a)
  if b not in y: y.add(b)
  else: y.remove(b)
print('%d %d' % (list(x)[0], list(y)[0]))

