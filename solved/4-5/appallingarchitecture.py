H, W = [int(x) for x in input().split()]

grid = [list(map(lambda x:x!='.', list(input()))) for _ in range(H)]

tot = 0
x_tot = 0
for row in grid:
  for i in range(W):
    if row[i]:
      x_tot += i+0.5
      tot += 1

avg = x_tot/tot

minX = grid[-1].index(True)
maxX = W-1 - grid[-1][::-1].index(True) + 1

if avg > maxX: print('right')
elif avg < minX: print('left')
else: print('balanced')

#print(grid, minX, maxX, avg)
