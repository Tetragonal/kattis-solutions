import math
EPS = 1e-12
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
def cross(p, q):
  return p.x*q.y-p.y*q.x
def projectPointOnLine(p,a,b):
  return a + (b-a)*((p-a)*(b-a))/((b-a)*(b-a))
def dist2(p1, p2):
  return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y)
def projectPointSegment(p,a,b):
  r = (b-a)*(b-a)
  if abs(r) < EPS: return a
  r = ((p-a)*(b-a))/r
  if r < 0: return a
  if r > 1: return b 
  return a + (b-a) * r
def distancePointSegment(p,a,b):
  return math.sqrt(dist2(p, projectPointSegment(p,a,b)))
def linesParallel(a,b,c,d):
  return abs(cross(b-a,c-d))<EPS
def linesColinear(a,b,c,d):
  return linesParallel(a,b,c,d) and abs(cross(a-b,a-c))<EPS and abs(cross(c-d,c-a))<EPS
def segmentsIntersect(a,b,c,d):
  if linesColinear(a,b,c,d):
    if dist2(a,c)<EPS or dist2(a,d)<EPS or dist2(b,c)<EPS or dist2(b,d)<EPS:
      return True
    return (c-a)*(c-b)<=0 or (d-a)*(d-b)<=0 or (c-b)*(d-b)<=0
  return cross(d-a,b-a)*cross(c-a,b-a)<=0 and cross(a-c,d-c)*cross(b-c,d-c)<=0

N = int(input())
for _ in range(N):
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  p1 = Point(x1,y1)
  p2 = Point(x2,y2)
  p3 = Point(x3,y3)
  p4 = Point(x4,y4)
  if segmentsIntersect(p1,p2,p3,p4):
    print('0.00')
  else:
    print('%.2f'%min(distancePointSegment(p1, p3, p4), 
            distancePointSegment(p2, p3, p4),
            distancePointSegment(p3, p1, p2),
            distancePointSegment(p4, p1, p2)))
