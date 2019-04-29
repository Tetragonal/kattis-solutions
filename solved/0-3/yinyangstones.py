s = input()
w = 0
for c in s:
    if c == 'W': w+=1
    else: w-=1
print(1 if w == 0 else 0)