
N = int(input())
arr = input().split()
good = True
for i,x in enumerate(arr):
  if x == 'mumble': continue
  elif int(x) != (i+1):
    print('something is fishy')
    good = False
    break

if good: print('makes sense')



