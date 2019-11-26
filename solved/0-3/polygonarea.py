import sys
import math

def convex_hull(points):
  if len(points) <= 1:
    return points
  def cross(o,a,b):
    return (a[0]-o[0]) * (b[1]-o[1]) - (a[1]-o[1]) * (b[0]-o[0])
  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2],lower[-1],p) <= 0:
      lower.pop()
    lower.append(p)
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2],upper[-1],p) <= 0:
      upper.pop()
    upper.append(p)
  return lower[:-1] + upper[:-1]
def computeSignedArea(p):
  area = 0
  for i in range(len(p)):
    j = (i+1)%len(p)
    area += p[i][0] * p[j][1] - p[j][0] * p[i][1]
  return area/2
lines = [x for x in sys.stdin]
i = 0
while i < len(lines):
  N = int(lines[i])
  if N == 0:
    break
  curr = [tuple(map(int,x.split())) for x in lines[i+1:i+N+1]]
  i += N+1
  area = computeSignedArea(curr)
  if area < 0:
    print('CW %.1f' % abs(area))
  else:
    print('CCW %.1f' % abs(area))
