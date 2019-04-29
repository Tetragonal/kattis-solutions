DROP = "DROP %d %d"
MOVE = "MOVE %d->%d %d"
TAKE = "TAKE %d %d"

while True:
  n = int(input())
  if n == 0: break
  commands = [input() for _ in range(n)]

  s1 = 0
  s2 = 0

  for line in commands:
    command, num = [x for x in line.split()]
    num = int(num)
    if command == 'DROP':
      print(DROP % (1, num))
      s1 += num
    
    if command == 'TAKE':
      if s2 >= num:
        print(TAKE % (2, num))
        s2 -= num
      else:
        if s2 > 0:  
          print(TAKE % (2, s2))
          num -= s2
        s2 = s1
        s1 = 0
        print(MOVE % (1, 2, s2))
        if num > 0:
          print(TAKE % (2, num))
          s2 -= num
  print()
