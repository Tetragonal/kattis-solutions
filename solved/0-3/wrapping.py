# https://github.com/INSAlgo/ICPC-Notebook/
import math
def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

# Assumes coords are listed clockwise/counterclockwise
def computeSignedArea(p):
  area = 0
  for i in range(len(p)):
    j = (i+1)%len(p)
    area += p[i][0]*p[j][1] - p[j][0] * p[i][1]
  return area / 2

def deg_to_rad(deg):
  return deg*math.pi/180
def rotate(x,y,angle):
  return (x*math.cos(angle)-y*math.sin(angle),
          y*math.cos(angle)+x*math.sin(angle))
def rotate_about_point(x,y,px,py,angle):
  x,y = rotate(x-px,y-py,angle)
  return (x+px,y+py)

T = int(input())
for _ in range(T):
  N = int(input())
  area = 0
  points = []
  for _ in range(N):
    x,y,w,h,v = map(float,input().split())
    area += w*h
    
    x1,y1 = rotate_about_point(x-w/2,y-h/2,x,y,deg_to_rad(-v))
    x2,y2 = rotate_about_point(x+w/2,y-h/2,x,y,deg_to_rad(-v))
    x3,y3 = rotate_about_point(x-w/2,y+h/2,x,y,deg_to_rad(-v))
    x4,y4 = rotate_about_point(x+w/2,y+h/2,x,y,deg_to_rad(-v))
    points += [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
  hull_area = abs(computeSignedArea(convex_hull(points)))
  print('%.1f %%' % (100*area/hull_area))


