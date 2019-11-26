input = raw_input 
def floyd_warshall(adj, V):
  dist = [[float('inf')]*V for _ in range(V)]
  for u in adj.keys():
    for v,w in adj[u]:
      dist[u][v] = min(w, dist[u][v])
  for i in range(V):
    dist[i][i] = min(0, dist[i][i])

  for k in range(V):
    for i in range(V):
      for j in range(V):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  # Correct nodes with negative cycles
  for k in range(V):
    for i in range(V):
      for j in range(V):
        if dist[j][j] < 0 and dist[k][j] != float('inf') != dist[j][i]:
          dist[k][i] = -float('inf')

  return dist
while True:
  N,M,Q = map(int, input().split())
  if N == M == Q == 0: break
  adj = dict()
  for _ in range(M):
    u,v,w = map(int, input().split())
    if u not in adj:
      adj[u] = []
    adj[u].append((v, w))

  dist = floyd_warshall(adj, N)

  for _ in range(Q):
    u,v = map(int, input().split())
    d = dist[u][v]
    if d == float('inf'):
      print('Impossible')
    elif d == -float('inf'):
      print('-Infinity')
    else:
      print(d)
  print('')

