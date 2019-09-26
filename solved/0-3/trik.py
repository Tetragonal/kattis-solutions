arr = [True, False, False]

def A(): arr[0], arr[1] = arr[1], arr[0]
def B(): arr[1], arr[2] = arr[2], arr[1]
def C(): arr[0], arr[2] = arr[2], arr[0]

for c in input():
  if c == 'A': A()
  elif c == 'B': B()
  elif c == 'C': C()
print(arr.index(True) + 1)
