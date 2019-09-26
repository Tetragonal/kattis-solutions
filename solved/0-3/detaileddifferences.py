T = int(input())
for _ in range(T):
  s = input()
  s2 = input()
  print(s)
  print(s2)
  print(''.join('.' if x==y else '*' for x,y in zip(s, s2)))
  print()

