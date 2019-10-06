while True:
  w, l = map(int, input().split())
  if w == l == 0:
    break

  n = int(input())
  x = y = 0
  realx = realy = 0
  for _ in range(n):
    cmd, dist = input().split()
    dist = int(dist)
    if cmd == 'u':
      y += dist
      realy = min(l-1, realy+dist)
    elif cmd == 'd':
      y -= dist
      realy = max(0, realy-dist)
    elif cmd == 'l':
      x -= dist
      realx = max(0, realx-dist)
    elif cmd == 'r':
      x += dist
      realx = min(w-1, realx+dist)
  print('Robot thinks %d %d' % (x,y))
  print('Actually at %d %d' % (realx, realy))
  print('')
