flag = False
while True:
  N = int(raw_input())
  if N == 0: break

  if flag: print('')
  flag = True

  arr1 = [int(raw_input()) for _ in range(N)]
  arr2 = [int(raw_input()) for _ in range(N)]

  d = {k:v for k,v in zip(sorted(arr1), sorted(arr2))}

  print('\n'.join([str(d[x]) for x in arr1]))
