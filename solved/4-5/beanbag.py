B = int(raw_input())
req = [int(x) for x in raw_input().split()]
T = int(raw_input())
farms = [[int(x) for x in raw_input().split()[1:]] for _ in range(T)]
#print(farms)
best = 9999999999

def f(arr):
  tot = 0
  for x in arr:
    tot += 1 << (x-1)
  return tot
farms = [f(x) for x in farms]

for i in range(2 ** B):
  #s = ("{:0%db}"%B).format(i)
  valid = True
  for farm in farms:
    if i & farm == 0:
      #print(s, farm)
      valid = False
      break
  if valid:
    #print('valid')
    tot = 0
    j = 0
    while i > 0:
      curr = i & 1
      if curr: tot += req[j]
      i = i >> 1
      j += 1
    best = min(best, tot)
print(sum(req) - best)
 
  


