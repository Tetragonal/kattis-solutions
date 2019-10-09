import collections
N = int(input())
vals = [x=='T' for x in input().split()]
exp = input().split()

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(len(exp)):
  if exp[i] in alp: exp[i] = vals[alp.index(exp[i])]

stack = collections.deque()

ops = ['*', '+', '-']

#print(exp)
for x in exp:
  #print(x, stack)
  if x in ops:
    if x == '*':
      arg1 = stack.pop()
      arg2 = stack.pop()
      stack.append(arg1 and arg2)
    elif x == '+':
      arg1 = stack.pop()
      arg2 = stack.pop()
      stack.append(arg1 or arg2)
    else:
      arg1 = stack.pop()
      stack.append(not arg1)
  else:
    stack.append(x)
print('F' if stack.pop() == False else 'T')
#print(stack)
