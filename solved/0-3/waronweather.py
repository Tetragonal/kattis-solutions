import math
EARTH_RADIUS = 40000./2/math.pi

def dist2(x,y,z,x2,y2,z2):
  return (x-x2)*(x-x2) + (y-y2)*(y-y2) + (z-z2)*(z-z2)

def in_range(x,y,z,sx,sy,sz):
  sat_dist = dist2(0,0,0,sx,sy,sz)
  max_dist = sat_dist - EARTH_RADIUS**2
  return dist2(x,y,z,sx,sy,sz) <= max_dist

while True:
  satellites = []
  K,M = map(int, input().split())
  if K==M==0: break
  for _ in range(K):
    x,y,z = map(float, input().split())
    satellites.append((x,y,z))

  ans = 0
  for _ in range(M):
    x,y,z = map(float, input().split())
    for sx,sy,sz in satellites:
      if in_range(x,y,z,sx,sy,sz):
        ans += 1
        break
  print(ans)

