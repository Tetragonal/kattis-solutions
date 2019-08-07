import math

while True:
  H, T = [int(x) for x in input().split()]
  if H == T == 0: break

  moves = 0
  if T % 2 == 0:
    moves += T//2
  else:
    moves += T//2 + 2
  H += math.ceil(T/2)

  if H % 2 == 0:
    print(moves + H//2)
  else:
    print(moves + H//2 + 4)

