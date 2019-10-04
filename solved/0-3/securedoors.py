N = int(input())

emp = set()
for _ in range(N):
  cmd, name = input().split()
  if cmd == 'entry':
    if name in emp:
      print('%s entered (ANOMALY)' % name)
    else:
      print('%s entered' % name)
      emp.add(name)
  else:
    if name in emp:
      print('%s exited' % name)
      emp.remove(name)
    else:
      print('%s exited (ANOMALY)' % name)


