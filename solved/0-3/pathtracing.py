import sys
lines = [line.strip() for line in sys.stdin.readlines()]
x = y = 0
minx = miny = maxx = maxy = 0
points = [(0,0)]
for line in lines:
  if line == "down": y += 1
  if line == "up": y -= 1
  if line == "left": x -= 1
  if line == "right": x += 1
  maxx = max(maxx, x)
  minx = min(minx, x)
  maxy = max(maxy, y)
  miny = min(miny, y)
  points.append((x,y))
points = list(map(lambda x: (1 + x[0] - minx, 1 + x[1] - miny), points))
grid = [[" "]*505 for x in range(505)]
for x,y in points:
  grid[y][x] = "*"

start = points[0]
end = points[-1]
grid[start[1]][start[0]] = "S"
grid[end[1]][end[0]] = "E"

ans = ""
for y in range(3+maxy-miny):
  for x in range(3+maxx-minx):
    if x == 0 or y == 0 or x == 2+maxx-minx or y == 2+maxy-miny:
      ans += "#"
    else:
      ans += grid[y][x]
  ans += "\n"
print(ans.strip())



