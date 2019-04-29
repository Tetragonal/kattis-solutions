# Return whether the array doesn't have duplicate 1-9
def check(arr):
  nums = set()
  for num in arr:  
    if num in nums: return False
    elif num != '.': nums.add(num)
  return True

# Return whether the board doesn't have duplicate 1-9
def check_board(grid):
  valid = True
  for row in range(9):
    valid = valid and check(grid[row])
  for col in range(9):
    valid = valid and check([row[col] for row in grid])
  for row in range(3):
    for col in range(3):
      a = []
      for i in range(3):
        for j in range(3):
          a.append(grid[3*row+i][3*col+j])
      valid = valid and check(a)
  return valid

# If check=True, return whether the board is valid
#   (No 3x3 where it's impossible to place a number in)
# Else, insert the next cross-hatch answer
def cross_hatch(grid, check=False):
  for num in range(1,10):
    rows = []
    cols = []
    for row in range(9):
      for col in range(9):
        if grid[row][col] == str(num):
          rows.append(row)
          cols.append(col)
    
    for row_b in range(3):
      for col_b in range(3):
        exist = False
        a = [[1,1,1],[1,1,1],[1,1,1]]
        for row in range(3):
          for col in range(3):
            if grid[3*row_b+row][3*col_b+col] != '.' \
                or 3*row_b+row in rows or 3*col_b+col in cols:
              a[row][col] = 0
            if grid[3*row_b+row][3*col_b+col] == str(num):
              exist = True
        tot = sum(map(sum,a))
        if check:
          if not exist and tot == 0: return False
          else: continue
        elif tot != 1 or exist:
          continue
        else:
          r_i = 0
          c_i = 0
          for r in range(3):
            for c in range(3):
              if a[r][c] == 1:
                r_i = r
                c_i = c
          grid[3*row_b+r_i][3*col_b+c_i] = str(num)
          return False 
  return True

def print_grid(grid):
  for row in grid:
    print(''.join(row))

def solve(grid):
  if not check_board(grid) or not cross_hatch(grid, check=True):
    print("ERROR")
    return False
  done = False
  while not done:
    done = cross_hatch(grid)
    if not cross_hatch(grid, check=True):
      print("ERROR")
      return False
  return True
grid = [[c for c in input()] for _ in range(9)]
if solve(grid):
  print_grid(grid)
