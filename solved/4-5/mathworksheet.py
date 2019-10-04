flag = False
while True:
  N = int(input())
  if N == 0: break
  arr = [str(eval(raw_input())) for _ in range(N)]

  if flag: print('')
  flag = True

  max_len = max(map(len, arr))

  num_cols = 51//(max_len+1)
  s = ''
  for i in range(len(arr)):
    s += ' ' * (max_len - len(arr[i])) + arr[i]
    if i == len(arr)-1: continue
    if i % num_cols == num_cols-1: s += '\n'
    else: s += ' '
  print(s)
  
