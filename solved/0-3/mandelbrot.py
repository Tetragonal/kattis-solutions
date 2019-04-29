import sys
import math

lines = [line.strip().split() for line in sys.stdin.readlines()]
lines = list(map(lambda x: (float(x[0]), float(x[1]), int(x[2])), lines))

def square(x, y):
   return (x**2 - y**2), (2*x*y)

def dist(x, y):
  return math.sqrt(x**2 + y**2)

for idx, (x, y, r) in enumerate(lines):
  idx += 1
  done = False
  x2, y2 = x, y
  for _ in range(r):
    if dist(x2, y2) > 2:
      print("Case %d: OUT" % idx)
      done = True
      break
    else:
      a, b = square(x2,y2)
      x2 = x + a
      y2 = y + b
  if not done:
    print("Case %d: IN" % idx)
  
      
