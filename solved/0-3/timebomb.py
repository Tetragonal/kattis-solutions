zero = [1,1,1,
        1,0,1,
        1,0,1,
        1,0,1,
        1,1,1]
one = [0,0,1,
       0,0,1,
       0,0,1,
       0,0,1,
       0,0,1]
two = [1,1,1,
       0,0,1,
       1,1,1,
       1,0,0,
       1,1,1]
three = [1,1,1,
         0,0,1,
         1,1,1,
         0,0,1,
         1,1,1]
four = [1,0,1,
        1,0,1,
        1,1,1,
        0,0,1,
        0,0,1]
five = [1,1,1,
        1,0,0,
        1,1,1,
        0,0,1,
        1,1,1]
six = [1,1,1,
       1,0,0,
       1,1,1,
       1,0,1,
       1,1,1]
seven = [1,1,1,
         0,0,1,
         0,0,1,
         0,0,1,
         0,0,1]
eight = [1,1,1,
         1,0,1,
         1,1,1,
         1,0,1,
         1,1,1]
nine = [1,1,1,
        1,0,1,
        1,1,1,
        0,0,1,
        1,1,1]
arr = []

def to_num(s1, s2, s3, s4, s5, i):
  i = i*4
  i2 = i+3
  a = s1[i:i2] + s2[i:i2] + s3[i:i2] + s4[i:i2] + s5[i:i2]
  a = [1 if x == '*' else 0 for x in a]
  if a == zero: return '0'
  elif a == one: return '1'
  elif a == two: return '2'
  elif a == three: return '3'
  elif a == four: return '4'
  elif a == five: return '5'
  elif a == six: return '6'
  elif a == seven: return '7'
  elif a == eight: return '8'
  elif a == nine: return '9'
  else: return False
nums = -1
for x in range(5):
  line = input()
  nums = (len(line)+1)//4
  arr.append(line)

s = ''
for i in range(nums):
  tmp = to_num(arr[0],arr[1],arr[2],arr[3],arr[4], i)
  if tmp:
    s += tmp
  else:
    print('BOOM!!')
    break
else:
  if int(s) % 6 == 0:
    print('BEER!!')
  else:
    print('BOOM!!')

