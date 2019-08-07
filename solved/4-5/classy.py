T = int(input())
for _ in range(T):
  N = int(input())

  arr = []
  for _ in range(N):
    inp = input().split()
    name, classes = inp[0][:-1], inp[1].split('-')[::-1]
    arr.append((name, classes))
  max_len = max(map(lambda x: len(x[1]), arr))

  for i, x in enumerate(arr):
    s = ""
    for c in x[1]:
      if c == 'upper': s += '1'
      elif c == 'middle': s += '2'
      elif c == 'lower': s += '3'
    while len(s) < max_len:
      s += '2'
    arr[i] = ((x[0],s))
  arr = sorted(arr, key=lambda x: (x[1], x[0]))
  print('\n'.join([x[0] for x in arr]))
  print('=' * 30)

