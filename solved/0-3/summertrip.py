s = input()

tot = 0
visited = [set()] * 26
for i,x in enumerate(s):
  c = ord(x) - ord('a')
  tot += len(visited[c])
  for st in visited: st.add(x)  
  visited[c] = set()
  
print(tot)
