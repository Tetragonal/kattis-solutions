import sys

fmt = "%d needs %d steps, %d needs %d steps, they meet at %d"

def collatz(x):
  if x % 2 == 0: return x // 2
  else: return 3 * x + 1

while True:
  line = sys.stdin.readline().strip()
  if line == "0 0": break
  a, b = [int(x) for x in line.strip().split()]
  orig_a, orig_b = a, b
  set_a = set([a])
  set_b = set([b])
  list_a = [a]
  list_b = [b]
  stop_a = False
  stop_b = False
  while True:
    if a in set_b:
      print(fmt % (orig_a, list_a.index(a), orig_b, list_b.index(a), a))
      break
    elif b in set_a:
      print(fmt % (orig_a, list_a.index(b), orig_b, list_b.index(b), b))
      break
    if a == 1: stop_a = True
    if b == 1: stop_b = True
    if not stop_a:
      a = collatz(a)
      set_a.add(a)
      list_a.append(a)
    if not stop_b:
      b = collatz(b)
      set_b.add(b)
      list_b.append(b)
