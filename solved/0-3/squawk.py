n,m,s,t = [int(x) for x in raw_input().split(' ')]
# n - # users
# m - num links
# s - initially infected user
# t - number of time steps 0 < t < 10

# Input connections
connections = [None] * n
for _ in range(m):
  a_idx, b_idx = [int(x) for x in raw_input().split(' ')]
  if connections[a_idx] is None:
    connections[a_idx] = []
  connections[a_idx].append(b_idx)
  if connections[b_idx] is None:
    connections[b_idx] = []
  connections[b_idx].append(a_idx)
#print(connections)

# Run t time steps
squawks = [0] * n
squawks[s] = 1
for _ in range(t):
  new_squawks = [0] * n
  for user_idx in range(n):
    if connections[user_idx] is None:
      continue
    for conn_idx in connections[user_idx]:
      new_squawks[user_idx] += squawks[conn_idx]
  squawks = new_squawks
print(sum(squawks))
