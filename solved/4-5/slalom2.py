W, V, N = [int(x) for x in raw_input().split()]

gates = []
for _ in range(N):
  gates.append(list(map(int,raw_input().split())))

S = int(input())

skis = []
for _ in range(S):
  skis.append(int(raw_input()))
skis = sorted(skis)

def p(vh):
  first_x, prev_y = gates[0]
  min_x = first_x
  max_x = first_x+W
  for x, y in gates[1:]:
    delta_y = y - prev_y
    delta_x = V * (delta_y/vh)

    if min_x - delta_x > x+W: return True
    if max_x + delta_x < x: return True

    min_x = max(min_x-delta_x, x)
    max_x = min(max_x+delta_x, x+W)

    prev_y = y
  return False

EPS = 1e-7
lo = 1.0
hi = 2e6
while hi - lo > EPS:
  mid = (lo + hi) / 2.0
  if p(mid): hi = mid
  else: lo = mid

mid = round(mid, 5)
if skis[0] > mid: print('IMPOSSIBLE')
else: print(max(x for x in skis if x <= mid))



