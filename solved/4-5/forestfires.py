import sys
def main():
  def find(vertice):
    a = []
    while parent[vertice] != vertice:
      a.append(vertice)
      vertice = parent[vertice]
    for x in a:
      parent[x] = vertice
    return parent[vertice]
  def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        parent[root2] = root1

  for line in sys.stdin:
    r, n = map(int, line.split())
    parent = range(10000)
    cnt = 0
    ans = []
    trees = [False]*10000
    tree_arr = []
    for i in range(n):
      # Place a tree
      m = -1
      while m == -1 or trees[m]:
        r = (r * 5171 + 13297) % 50021
        m = r % 10000
      trees[m] = True
      tree_arr.append(m)
      if m-100>=0 and trees[m-100]:
        union(m, m-100)
      if m+100<10000 and trees[m+100]:
        union(m, m+100)
      if m-1>=0 and m%100!=0 and trees[m-1]:
        union(m, m-1)
      if m+1<10000 and m%100!=99 and trees[m+1]:
        union(m, m+1)
      
      # Choose A
      r = (r * 5171 + 13297) % 50021
      A = tree_arr[r % (i + 1)]
      # Choose B
      r = (r * 5171 + 13297) % 50021
      B = tree_arr[r % (i + 1)]
      
      # Fire query
      if find(A) == find(B): 
        cnt += 1
      if i % 100 == 99:
        ans.append(cnt)
        cnt = 0
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
  main()
