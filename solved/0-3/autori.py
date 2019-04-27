line = input()
ans = line[0]
for i in range(1, len(line)):
  if line[i-1] == '-': ans += line[i]
print(ans)
