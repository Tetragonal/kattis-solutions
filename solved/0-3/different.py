import sys

lines = [line.strip().split() for line in sys.stdin.readlines()]
for line in lines:
  x, y = int(line[0]), int(line[1])
  print(abs(x-y))

