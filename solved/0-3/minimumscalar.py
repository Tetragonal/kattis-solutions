T = int(input())

for case in range(T):
  input()

  a1 = [int(x) for x in input().split()]
  a2 = [int(x) for x in input().split()]
  a1 = sorted(a1)
  a2 = sorted(a2, reverse=True)

  tot = 0
  for x, y in zip(a1, a2): tot += x*y
  print("Case #%d: %d" % (case+1, tot))