n = input()
stops = [int(x) for x in input().split()]
a = [False] * 1005
for stop in stops:
  a[stop] = True

start = -1
i = 0
while i < len(a):
  if a[i]:
    start = i
    while a[i]:
      i += 1
  else:
    if start > 0:
      if i - start > 2:
        print("%d-%d" % (start, i-1), end=" ")
      elif i - start == 2:
        print("%d %d" % (i-2, i-1), end=" ")
      elif i - start == 1:
        print (i-1, end=" ") 
    i += 1
    start = -1
