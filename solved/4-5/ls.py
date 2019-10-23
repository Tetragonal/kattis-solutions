s = input()
split = [x for x in s.split('*') if x != '']
P = int(input())
arr = [input() for _ in range(P)]
for x in arr:
  orig_x = x
  i = 0
  j = 0
  offset = 0
  if '*' not in s:
    if x == s: print(x)
    else: continue
  if s[0] != '*':
    if split[0] != x[:len(split[0])]:
      continue
    else:
      j += 1
      x = x[len(split[0]):]
  if s[-1] != '*':
    if split[-1] != x[-len(split[-1]):]:
      continue
    else:
      x = x[:-len(split[-1])]
      offset += 1
  while j + offset < len(split) and x.find(split[j]) != -1:
    x = x[x.find(split[j])+1:]
    j += 1
  if j + offset == len(split):
    print(orig_x)
