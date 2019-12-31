#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+1, INF = 1e9;
struct edge {int v, c, f;};

int n, src, snk, h[N], ptr[N];
vector<edge> edgs;
vector<int> g[N];

void add_edge (int u, int v, int c) {
  int k = edgs.size();
  edgs.push_back({v, c, 0});
  edgs.push_back({u, 0, 0});
  g[u].push_back(k);
  g[v].push_back(k+1);
}

bool bfs() {
  memset(h, 0, sizeof h);
  queue<int> q;
  h[src] = 1;
  q.push(src);
  while(!q.empty()) {
    int u = q.front(); q.pop();
    for(int i : g[u]) {
      int v = edgs[i].v;
      if (!h[v] and edgs[i].f < edgs[i].c)
        q.push(v), h[v] = h[u] + 1;
    }
  }
  return h[snk];
}

int dfs (int u, int flow) {
  if (!flow or u == snk) return flow;
  for (int &i = ptr[u]; i < g[u].size(); ++i) {
    edge &dir = edgs[g[u][i]], &rev = edgs[g[u][i]^1];
    int v = dir.v;
    if (h[v] != h[u] + 1)  continue;
    int inc = min(flow, dir.c - dir.f);
    inc = dfs(v, inc);
    if (inc) {
      dir.f += inc, rev.f -= inc;
      return inc;
    }
  }
  return 0;
}

int dinic() {
  int flow = 0;
  while (bfs()) {
    memset(ptr, 0, sizeof ptr);
    while (int inc = dfs(src, INF)) flow += inc;
  }
  return flow;
}

int main() {
  int n, m, c;
  cin >> n >> m >> c;
  vector<string> input;
  for(int i = 0; i < m; i++) {
    string in;
    cin >> in;
    input.push_back(in);
  }
  map<char, int> costs;
  costs['.'] = INF;
  costs['B'] = INF;
  for(int i = 0; i < c; i++) {
    int cost;
    cin >> cost;
    costs['a'+i] = cost;
  }
  
  snk = N-5;

  for(int i = 0; i < m; i++) {
    for(int j = 0; j < n; j++) {
      int vidx = i*n + j;
      int idx = vidx + n*m;
      if(input[i][j] == 'B') {
        src = vidx;
      }
      add_edge(vidx, idx, costs[input[i][j]]);

      if((i==0) || (j==0) || (i==m-1) || (j==n-1)) {
        add_edge(idx, snk, INF);
      } else { 
        if(j!=n-1) add_edge(idx, vidx+1, INF); 
        if(j!=0) add_edge(idx, vidx-1, INF); 
        if(i!=m-1) add_edge(idx, vidx+n, INF); 
        if(i!=0) add_edge(idx, vidx-n, INF); 
      }

    }
  }
  int maxflow = dinic();
  if(maxflow >= INF) {
    cout << -1 << endl;
  } else {
    cout << maxflow << endl;
  }

}

