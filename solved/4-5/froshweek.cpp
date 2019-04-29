#include <bits/stdc++.h>

using namespace std;

const int SIZE = 1000005;

#define LSB(i) ((i) & -(i)) // zeroes all the bits except the least significant one

int A[SIZE];

int sum(int i) // Returns the sum from index 1 to i
{
    int sum = 0;
    while (i > 0) 
        sum += A[i], i -= LSB(i);
    return sum;
}
 
void add(int i, int k) // Adds k to element with index i
{
    while (i < SIZE) 
        A[i] += k, i += LSB(i);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;

  unordered_map<int, int> to_idx;
  vector<int> sorted;

  int id;
  for(int i = 0; i < n; i++){
    cin >> id;
    sorted.push_back(id); 
    to_idx[id] = i + 1;
  }
  
  sort(sorted.begin(), sorted.end());

  for(int i = 0; i < n; i++) add(i+1, 1);

  long long totalSwaps = 0;
  for(int i = 0; i < n; i++){
    id = sorted[i];
    add(to_idx[id], -1);
    int swaps = sum(to_idx[id]);
    totalSwaps += swaps;
    // cout << id << " " << to_idx[id] << " " << swaps << endl;
  }

  cout << totalSwaps << endl;
  return 0;
}
