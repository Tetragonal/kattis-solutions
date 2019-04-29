#include <bits/stdc++.h>
using namespace std;

int main(){
  string line;
  while (getline(cin, line))
  {
    int n = stoi(line, NULL);
    if(n == 0) return 0;
    vector<vector<string>> collisions(10000);
    set<string> uniq;
    for(int i = 0; i < n; i++){
      getline(cin, line);
      char hash = 0;
      for (char& c : line){
        hash = hash ^ c;
      }
      collisions[hash].push_back(line);
      uniq.insert(line);
    }
    int totalCollisions = 0;
    for(int i = 0; i < collisions.size(); i++){
      for(int j = 0; j < collisions[i].size(); j++){
        for(int k = j+1; k < collisions[i].size(); k++){
          if(collisions[i][j] != collisions[i][k]){
            totalCollisions += 1;
          }
        }
      }
    }
    cout << uniq.size() << " " << totalCollisions << endl;
  }

  
  

} 
