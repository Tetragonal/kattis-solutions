ops = ['+', '-', '//', '*']

def solve(n):
  for op1 in range(4):
    for op2 in range(4):
      for op3 in range(4):
        s = '4 %s 4 %s 4 %s 4' % (ops[op1], ops[op2], ops[op3])
        if eval(s) == n:
          return s.replace('//','/') + ' = %d' % n
  return 'no solution'
N = int(input())
for _ in range(N):
  x = int(input())
  print(solve(x))


