import sys
while True:
  line = sys.stdin.readline().strip()
  if line == "0": break
  perm = [int(x) for x in line.split()][1:]
  message = input()
  if len(message) % len(perm) != 0:
    message += " " * (len(perm) - (len(message) % len(perm)))
  ans = ""
  for i in range(len(message)//len(perm)):
    chunk = message[i*len(perm):(i+1)*len(perm)]
    for j in perm:
      ans += chunk[j-1]
  print("'%s'" % ans) 
