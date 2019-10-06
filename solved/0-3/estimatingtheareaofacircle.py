PI = 3.141592653589

while True:
  r, m, c = [float(x) for x in raw_input().split()]
  if r == m == c == 0: break
  print('%0.8f %0.8f' % (PI*r*r, 2*r*2*r * (c/m)))




