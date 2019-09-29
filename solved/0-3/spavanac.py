h, m = [int(x) for x in input().split()]
h += 23
m += 15
if m > 60:
  h += 1
  m -= 60
if h > 23:
  h -= 24
print(h,m)


