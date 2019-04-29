n = int(input())

lines = [input().split() for _ in range(n)]


state = []
dream_idx = dict()

for line in lines:
  command = line[0]

  # add e to stack, add position to map
  if command == 'E':
    state.append(line[1])
    dream_idx[line[1]] = len(state)
  # pop r elements from stack and delete from map
  elif command == 'D':
    for _ in range(int(line[1])):
      del dream_idx[state[-1]]
      state.pop()
  # for all ! and non-! in map, find lowest, highest one in the stack
  # if ! lower than highest non-!, plot error
  # otherwise, dream (size - !-low)
  elif command == 'S':
    events = line[2:]
    high = -1
    low_neg = 1e9
    plot_error = False

    for e in events:
      neg = e[0] == '!'
      if neg: e = e[1:]

      # Event doesn't exist -> plot error
      if not neg and e not in dream_idx:
        plot_error = True
        break
      # set lowest ! and non-! idx        
      elif neg and e in dream_idx and dream_idx[e] < low_neg: low_neg = dream_idx[e]
      elif not neg and dream_idx[e] > high: high = dream_idx[e]
    
    if plot_error:
      print('Plot Error')
    elif low_neg == 1e9:
      print('Yes')
    elif low_neg <= high:
      print('Plot Error')
    else:
      print("%d Just A Dream" % (len(state) - low_neg + 1))
