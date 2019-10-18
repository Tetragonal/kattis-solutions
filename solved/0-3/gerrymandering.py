import collections
# Return win, wa, wb
def calc(a, b):
  tot = a+b
  if a > b:
    return ('A', a-int((a+b)/2+1), b)
  else:
    return ('B', a, b-int((a+b)/2+1))

def efficiency(wa, wb, v):
  return abs(wa-wb)/v

P, D = map(int, input().split())

tot = 0
cntA = collections.Counter()
cntB = collections.Counter()
for _ in range(P):
  d, a, b = map(int, input().split())
  cntA[d-1] += a
  cntB[d-1] += b
  tot += a+b

tot_wa = 0
tot_wb = 0
for i in range(D):
  win, wa, wb = calc(cntA[i], cntB[i])
  tot_wa += wa
  tot_wb += wb
  print('%s %d %d' % (win, wa, wb))

print(efficiency(tot_wa, tot_wb, tot))



