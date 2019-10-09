import sys
import collections
facs = dict()
def fac(n):
  if n <= 1: return 1
  if n not in facs:
    facs[n] = n * fac(n-1)
  return facs[n]

for line in sys.stdin:
  line = line[:-1]
  cnt = collections.Counter(line)
  tot = fac(len(line))  
  for v in cnt.values():
    tot //= fac(v)
  print(tot)
