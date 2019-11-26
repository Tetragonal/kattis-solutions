#include <bits/stdc++.h>
using namespace std;

#define Point pair<double, double>

inline double cross(Point o, Point a, Point b) {
  return (a.first - o.first) * (b.second - o.second) - (a.second - o.second) * (b.first - o.first);
}

vector<Point> convex_hull(vector<Point> points) {
  if (points.size() <= 1) return points;
  sort(points.begin(), points.end());
  vector<Point> upper;
  for(int i = points.size()-1; i >= 0; i--) {
    Point p = points[i];
    while((upper.size() >= 2) && (cross(upper[upper.size()-2], upper[upper.size()-1], p) <= 0)){
      upper.pop_back();
    }
    upper.push_back(p);
  }
  return upper;
}

int main() {
  int N;
  double B;
  cin >> N >> B;

  vector<Point> points;
  
  for(int i = 0; i < N; i++){
    double c, h, p;
    cin >> c >> h >> p;
    points.push_back(make_pair(B*h/c, B*p/c));
  }
  points = convex_hull(points);
  double best = 0;
  cout.precision(17);
  for(int i = 0; i < points.size()-1; i++){
    Point p1 = points[i];
    Point p2 = points[i+1];
    double A = p1.first;
    double B = p2.first;
    double C = p1.second;
    double D = p2.second;
    double a = (A*C+B*D-A*D-B*C);
    double b = (A*D+B*C-2*B*D);
    double x = max(0., min(1., -b/(2*a)));
    double y = ((A*x)+(B*(1-x))) * ((C*x)+(D*(1-x))); 
    best = max(y, best);
  }
  cout << best << endl;
}
