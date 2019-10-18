import math
from decimal import *
getcontext().prec = 17
N = int(input())
EPS = Decimal(1e-7)
for _ in range(N):
  W, G, H, R = map(Decimal,input().split())
  G, H = min(G,H), max(G,H)
  min_len = (W*W + (H-G)*(H-G)).sqrt()
  if R==G or R==H:
    max_len = min_len
  else:
    def sim(r,g,d):
      x = (-r*d)/(r-g)
      return (g-r)/g *((d+x)*(d+x) + g*g).sqrt()

    def p(d):
      return sim(R,G,d) + sim(R,H,W-d)
    lo = Decimal(0.0)
    hi = W
    while abs(hi-lo) > EPS:
      lt = lo + (hi - lo) / Decimal(3.0)
      rt = hi - (hi - lo) / Decimal(3.0)
      if p(lt) > p(rt):
        lo = lt
      else:
        hi = rt
    max_len = p(lo)
  print('%0.7f %0.7f' % (min_len, max_len))
