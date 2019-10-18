import math
class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self, o):
    return Point(self.x+o.x, self.y+o.y)
  def __sub__(self, o):
    return Point(self.x-o.x, self.y-o.y)
  def __mul__(self, o):
    if isinstance(o, float): return Point(o*self.x, o*self.y)
    return self.x*o.x + self.y*o.y
  def __truediv__(self, o):
    return Point(self.x/o, self.y/o)
def projectPointOnLine(p,a,b):
  return a + (b-a)*((p-a)*(b-a))/((b-a)*(b-a))
def dist(p1, p2):
  return math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))

N = int(input())
points = [input().split() for _ in range(N)]
points = [Point(float(x), float(y)) for x,y in points]
lo = float('inf') 
d = dict()
for i in range(N):
  hi = float('-inf')
  p2 = points[i]
  p3 = points[(i+1)%N]
  for j in range(N):
    p1 = points[j]
    if i == j or (i+1)%N == j: continue
    p_proj = projectPointOnLine(p1,p2,p3)
    hi = max(hi, dist(p1, p_proj))
  lo = min(hi,lo)
print(lo)
