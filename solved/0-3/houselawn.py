L, M = [int(x) for x in input().split()]

arr = [input().split(',') for _ in range(M)]
def poss(c,t,r):
  return (c*t) * 10080 >= L * (t+r)
arr = [x for x in arr if poss(int(x[2]), int(x[3]), int(x[4]))]

if len(arr) == 0:
  print('no such mower')
else:
  lo = min([int(x[1]) for x in arr])
  ans = [x[0] for x in filter(lambda x: int(x[1]) == lo, arr)]
  print('\n'.join(ans))
