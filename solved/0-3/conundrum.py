s = input()
cnt = 0
for i,x in enumerate(s):
  if i % 3 == 0:
    if x != 'P': cnt += 1
  elif i % 3 == 1:
    if x != 'E': cnt += 1
  else:
    if x != 'R': cnt += 1
print(cnt)
