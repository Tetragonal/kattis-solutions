#include <bits/stdc++.h>
using namespace std;

#define LSB(i) ((i) & -(i)) // zeroes all the bits except the least significant one
#define SIZE 20005
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
int bsearch(int k) { // Find lowest element with value k
  int lo = 0;
  int hi = SIZE-1;
  while(lo <= hi){
    int mid = (lo+hi)/2;
    int cnt = sum(mid);
    if(cnt < k) lo = mid+1;
    else if(cnt > k) hi = mid-1;
    else if(lo != mid) hi = mid;
    else return mid;
  }
  return -1;
}

int subseq(string str1, string str2) // find lowest index of str2 such that str1 is a subseq, or -1 if N/A
{ 
   int j = 0;
   int i = 0;
   for (; i<str2.length()&&j<str1.length(); i++) 
       if (str1[j] == str2[i]) 
         j++; 
   return (j==str1.length()) ? i : -1; 
} 


int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  string S;
  cin >> S;

  int n, q;
  cin >> n >> q;

  // sort words lexicographically
  vector<string> words(n);
  for(int i = 0; i < n; i++) cin >> words[i];
  sort(words.begin(), words.end()); 

  vector<tuple<int, int, int>> queries(q);
  for(int i = 0; i < q; i++) {
    int tmp1, tmp2, tmp3;
    cin >> tmp1 >> tmp2 >> tmp3;
    queries[i] = make_tuple(tmp1, tmp2, tmp3);
  }

  // group queries based on left index
  map<int, vector<int>> d;
  for(int i = 0; i < q; i++) {
    tuple<int,int,int> t = queries[i];
    d[get<0>(t)].push_back(i);
  }

  vector<int> ans(q);
	for (auto it = d.begin(); it != d.end(); it++ ) {
    for(int i = 0; i < SIZE; i++) A[i] = 0;

    int l = it->first - 1;

    // sort based on increasing right index
    sort(it->second.begin(), it->second.end(), [&queries](const int lhs, const int rhs)
    {
      return get<1>(queries[lhs]) < get<1>(queries[rhs]);
    });

    // for each word, find the smallest right index required for it to be a subsequence
    vector<tuple<int,int>> breakpoints;
    for(int i = 0; i < words.size(); i++){
      string w = words[i];
      int loc = subseq(w, S.substr(l));
      if(loc == -1) continue;
      breakpoints.push_back(make_tuple(loc+l, i));
    }

    // sort based on increasing required index
    sort(breakpoints.begin(), breakpoints.end(), [](const tuple<int,int> lhs, const tuple<int,int> rhs)
    {
      return get<0>(lhs) < get<0>(rhs);
    });
    
    // go through queries in increasing right index, add to BIT when a word becomes a subsequence
    int curr = 0;
    for (int i = 0; i < it->second.size(); i++) {
      int l, r, k;
      tie(l,r,k) = queries[it->second[i]];
      while(curr < breakpoints.size() && get<0>(breakpoints[curr]) <= r) {
        add(get<1>(breakpoints[curr])+1, 1);
        curr += 1;
      }
      // search for the kth element in the BIT
      ans[it->second[i]] = bsearch(k) - 1;
    }
	}

  //print ans
  for (int i = 0; i < ans.size(); i++){
    if(ans[i] < 0) cout << "NO SUCH WORD" << endl;
    else {
      string word = words[ans[i]];
      if(word.length() <= 10) cout << word << endl;
      else cout << word.substr(0,10) << endl;
    }
  }
}
