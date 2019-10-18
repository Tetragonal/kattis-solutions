N = int(input())

s = set(int(input()) for _ in range(N))


flag = False
for i in range(1,max(s)):
  if i not in s:
    print(i)
    flag = True
if not flag:
  print('good job')

