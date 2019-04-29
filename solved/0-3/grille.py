def impossible():
  print('invalid grille')
  exit()

def rotate_cw(grille_arr):
  new_grille_arr = [[0]*n for x in [0]*n]
  new_grille_str = ''
  
  for r in range(n):
    for c in range(n):
      new_grille_arr[c][n-1-r] = grille_arr[r][c] 

  for r in range(n):
    for c in range(n):
      new_grille_str += new_grille_arr[r][c] 
  #print(new_grille_str)

  return new_grille_arr, new_grille_str

#########################

n = int(raw_input())

print_arr = [[0]*n for x in [0]*n]

grille_arr = []
grille_str = ''
for _ in range(n):
  line = raw_input()
  grille_arr.append(line)
  grille_str += line
count = sum([(1 if x=='.' else 0) for x in grille_str])
#print(grille_arr)
#print(count)

enc_str = raw_input()
enc_idx = 0

for _ in range(4):
  # Populate print_idx for the first
  for idx, c in enumerate(grille_str):
    if c == '.':
      x_idx = idx % n
      y_idx = idx / n
  
      if print_arr[y_idx][x_idx] != 0:
        impossible()

      #print(print_arr, y_idx, x_idx)
      #print(print_arr[y_idx][x_idx])
      #print(enc_str[enc_idx])
      print_arr[y_idx][x_idx] = enc_str[enc_idx]
      enc_idx += 1

  grille_arr, grille_str = rotate_cw(grille_arr)


final_str = ''
for r in range(n):
  for c in range(n):
    if(print_arr[r][c] == 0):
      impossible()
    final_str += print_arr[r][c]
print(final_str)



  

  
