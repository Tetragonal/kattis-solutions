#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll INF = 4000000000;
const int BREAKPOINT = 35;
const ll MAX_ARRAY_LEN = 1500000;

// Standard knapsack dp
ll knapsack1(const vector<ll> &vals, const vector<ll> &costs, ll capacity) {
  capacity = min(capacity, MAX_ARRAY_LEN);
	ll** dp = new ll*[2];
  dp[0] = new ll[capacity+1];
  dp[1] = new ll[capacity+1];
	memset(dp[0], 0, sizeof(ll)*(capacity+1));
	memset(dp[1], 0, sizeof(ll)*(capacity+1));
	
	for(int i = 0; i < vals.size(); i++){
		int curr = i % 2 == 1;
		int prev = i % 2 == 0;

		for(ll j = 1; j <= capacity; j++) {
			if(costs[i] <= j) {
				dp[curr][j] = max(vals[i] + dp[prev][j-costs[i]], dp[prev][j]);
			} else {
				dp[curr][j] = dp[prev][j];
			}
		}
	}
  return dp[vals.size() % 2 == 0][capacity];
}

// n x v knapsack dp
ll knapsackV(const vector<ll> &vals, const vector<ll> &costs, ll capacity) {
  ll size = 1;
  for(int i = 0; i < vals.size(); i++) size += vals[i];
  size = min(size, MAX_ARRAY_LEN);
	ll* dp = new ll[size];
	
  for(int i = 0; i <= vals[0]; i++) dp[i] = costs[0] > capacity ? INF : costs[0];
  for(int i = vals[0]+1; i < size; i++) dp[i] = INF;

	for(int i = 1; i < vals.size(); i++){
    if(costs[i] > capacity) continue;
    dp[size-1] = min(dp[size-1], dp[size-1 - vals[i]] + costs[i]);
    if (dp[size-1] > capacity) dp[size-1] = INF;
		for(ll j = size-2; j-vals[i] >= 0; j--) {
		  dp[j] = min(min(dp[j], dp[j-vals[i]] + costs[i]), dp[j+1]);
      if (dp[j] > capacity) dp[j] = INF;
		}
    for(int j = vals[i]; j >= 0; j--) dp[j] = min(min(dp[j], dp[j+1]),costs[i]);
	}
  int i = -1;
  while (i+1 < size && dp[i+1] != INF) i++;
  return max(0,i);
}

// Meet-in-the-middle brute force
ll knapsack2(const vector<ll> &vals, const vector<ll> &costs, ll capacity) {
  map<ll,ll> costToValue;
  int half = costs.size() == 1 ? 1 : vals.size() / 2;
  for(int subset = 0; subset < (1 << half); subset++) {
    ll totVal = 0;
    ll totCost = 0; 
    for(int i = 0; i < half; i++){
      if((subset & (1 << i)) != 0) {
        totVal += vals[i];
        totCost += costs[i];
      }
    }
    if(totCost <= capacity && (costToValue.find(totCost) == costToValue.end() || costToValue[totCost] < totVal)) {
      costToValue[totCost] = totVal;
    }
  }
  
  ll bestVal = 0;
  vector<ll> subsetCosts;
  vector<ll> subsetVals;
  for(auto elem : costToValue) {
    ll cost = elem.first;
    ll val = elem.second;
    if(val > bestVal || bestVal == 0) {
      subsetCosts.push_back(elem.first);
      subsetVals.push_back(elem.second);
    }
    bestVal = max(bestVal, val);
  }

  int sndHalf = vals.size() - half;
  for(int subset = 0; subset < (1 << (sndHalf)); subset++) {
    ll totVal = 0;
    ll totCost = 0;
    for(int i = 0; i < sndHalf; i++) {
      if((subset & (1 << i)) != 0) {
        totVal += vals[half + i];
        totCost += costs[half + i];
      }
    }
    // Binary search for best in subsets
    auto rit = lower_bound(subsetCosts.rbegin(), subsetCosts.rend(), capacity - totCost, greater<ll>());
    if(rit == subsetCosts.rend()) continue;
    auto idx = distance(subsetCosts.begin(), rit.base())-1;
    if(idx >= 0 && idx < subsetCosts.size()) {
      bestVal = max(bestVal, subsetVals[idx] + totVal);
    }
  }
  return bestVal;
}


int main() {
  int T, n;
  ll C;
  cin >> T;
  for(int i = 0; i < T; i++){
    cin >> n >> C;
    vector<ll> values(n);
    vector<ll> costs(n);
    
    for(int i = 0; i < n; i++) {
      cin >> values[i];
    }
    for(int i = 0; i < n; i++) {
      cin >> costs[i];
    }
    
    if(n >= BREAKPOINT) {
      cout << knapsackV(values, costs, C) << endl;
    } else {
	    cout << knapsack2(values, costs, C) << endl;
    }
    
  }
	return 0;
}
