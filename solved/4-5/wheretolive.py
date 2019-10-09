MAX_SIZE = 1005

while True:
  N = int(raw_input())
  if N == 0: break
  coords = [[int(x) for x in raw_input().split()] for _ in range(N)]


  def p(i, j):
    return sum([(((x-i)**2)+((y-j)**2)) for x,y in coords])

  minx = 0
  maxx = MAX_SIZE-1
  while minx < maxx:
    mid = (minx + maxx)//2
    if p(0,mid) > p(0,mid+1):
      minx = mid+1
    else:
      maxx = mid
  
  miny = 0
  maxy = MAX_SIZE-1
  while miny < maxy:
    mid = (miny+maxy)//2
    if p(mid,0) > p(mid+1,0):
      miny = mid+1
    else:
      maxy = mid

  while miny > 0 and p(miny-1,minx) == p(miny,minx): miny -= 1
  while minx > 0 and p(miny,minx-1) == p(miny,minx): minx -= 1
  while minx > 0 < miny and p(miny-1,minx-1) == p(miny,minx):
    minx -= 1
    miny -= 1

  print('%d %d' % (miny, minx))
