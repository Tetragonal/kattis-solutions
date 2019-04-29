A = int(raw_input())

def clamp(x, l, r):
  return min(r, max(x, l))

for _ in range(A):
  N, T = [int(x) for x in raw_input().split()]
  arr =  [int(x) for x in raw_input().split()]

  fastest = [0] + [-1] * (7205)
  it = 1
  done = False
  mod = [0]
  while not done:
    mod_old = mod[:]
    mod = []
    done = True
    for i in mod_old:
      for e in arr:
        n = clamp(i+e, 0, 3600)
        if fastest[n] == -1:
          fastest[n] = it
          mod.append(n)
          done = False
    it += 1
  if fastest[T] != -1:
    print('%d %d' % (fastest[T], 0))
  else:
    i = T
    while i <= 3600:
      if fastest[i] != -1:
        print('%d %d' % (fastest[i], i-T))
        break
      i += 1