from heapq import *

while True:
  h, w = map(int, input().split())
  if h == w == 0:
    break
  blocks = [[int(x) for x in input()] for _ in range(h)]
  prev = [[False]*w for _ in range(h)]
  prev[0] = [(-1, -1)]*w
  q = [(blocks[0][x], (0,x)) for x in range(w)]
  heapify(q)

  end_r = -1
  enc_c = -1
  while len(q) > 0:
    cost,(r,c) = heappop(q)
    if r == h-1: 
      end_r = r
      end_c = c
      break
    # + directions
    if r-1 >= 0 and not prev[r-1][c]:
      heappush(q, (cost+blocks[r-1][c], (r-1,c)))
      prev[r-1][c] = (r,c)
    if r+1 < h and not prev[r+1][c]:
      heappush(q, (cost+blocks[r+1][c], (r+1,c)))
      prev[r+1][c] = (r,c)
    if c-1 >= 0 and not prev[r][c-1]:
      heappush(q, (cost+blocks[r][c-1], (r,c-1)))
      prev[r][c-1] = (r,c)
    if c+1 < w and not prev[r][c+1]:
      heappush(q, (cost+blocks[r][c+1], (r,c+1)))
      prev[r][c+1] = (r,c)
    # x directions
    if r-1 >= 0 and c-1 >= 0 and not prev[r-1][c-1]:
      heappush(q, (cost+blocks[r-1][c-1], (r-1,c-1)))
      prev[r-1][c-1] = (r,c)
    if r+1 < h and c-1 >= 0 and not prev[r+1][c-1]:
      heappush(q, (cost+blocks[r+1][c-1], (r+1,c-1)))
      prev[r+1][c-1] = (r,c)
    if r-1 >= 0 and c+1 < w and not prev[r-1][c+1]:
      heappush(q, (cost+blocks[r-1][c+1], (r-1,c+1)))
      prev[r-1][c+1] = (r,c)
    if r+1 < h and c+1 < w and not prev[r+1][c+1]:
      heappush(q, (cost+blocks[r+1][c+1], (r+1,c+1)))
      prev[r+1][c+1] = (r,c)

  blocks = [[str(x) for x in row] for row in blocks]
  while end_r != -1:
    blocks[end_r][end_c] = " "
    end_r, end_c = prev[end_r][end_c]
  print('\n'.join([''.join(row) for row in blocks]) + '\n')
