C = []
def find(x):
  if C[x][0] == x:
    return x
  else:
    C[x] = (find(C[x][0]), C[x][1])
    return C[x][0]
def merge(x, y):
  x = find(x)
  y = find(y)
  if x == y: return C[y][1]
  if C[x][1] > C[y][1]: x,y = y,x
  val = C[x][1]
  C[x] = (C[y][0], C[x][1])
  C[y] = (C[y][0], C[y][1] + val)
  return C[y][1]
T = int(raw_input())
for _ in range(T):
  F = int(raw_input())
  C = list(zip(range(F*2), [1]*(F*2)))
  curr = 0
  p_to_id = dict()
  for _ in range(F):
    x, y = [x for x in raw_input().split()]
    if x not in p_to_id:
      p_to_id[x] = curr
      curr += 1
    if y not in p_to_id:
      p_to_id[y] = curr
      curr += 1
    
    print(merge(p_to_id[x], p_to_id[y]))

