// FFT
// https://github.com/IMEplusplus/icpc-notebook/blob/master/math/fft-tourist.cpp 
// https://www.mpi-inf.mpg.de/fileadmin/inf/d1/teaching/summer16/polycomp/polycomp06.pdf
#include <bits/stdc++.h>
using namespace std;

typedef long double dbl;
typedef long long ll;
const int MAXN = 200000;
const int U = 50000+5;

struct num {
	dbl x, y;
	num() { x = y = 0; }
	num(dbl x, dbl y) : x(x), y(y) {}
};

inline num operator+ (num a, num b) { return num(a.x + b.x, a.y + b.y); }
inline num operator- (num a, num b) { return num(a.x - b.x, a.y - b.y); }
inline num operator* (num a, num b) { return num(a.x * b.x - a.y * b.y, a.x * b.y + a.y * b.x); }
inline num conj(num a) { return num(a.x, -a.y); }

int base = 1;
vector<num> roots = {{0, 0}, {1, 0}};
vector<int> rev = {0, 1};

const dbl PI = acosl(-1.0);

void ensure_base(int nbase) {
	if(nbase <= base) return;

	rev.resize(1 << nbase);
	for(int i=0; i < (1 << nbase); i++) {
		rev[i] = (rev[i >> 1] >> 1) + ((i & 1) << (nbase - 1));
	}
	roots.resize(1 << nbase);

	while(base < nbase) {
		dbl angle = 2*PI / (1 << (base + 1));
		for(int i = 1 << (base - 1); i < (1 << base); i++) {
			roots[i << 1] = roots[i];
			dbl angle_i = angle * (2 * i + 1 - (1 << base));
			roots[(i << 1) + 1] = num(cos(angle_i), sin(angle_i));
		}
		base++;
	}
}
void fft(vector<num> &a, int n = -1) {
	if(n == -1) {
		n = a.size();
	}
	assert((n & (n-1)) == 0);
	int zeros = __builtin_ctz(n);
	ensure_base(zeros);
	int shift = base - zeros;
	for(int i = 0; i < n; i++) {
		if(i < (rev[i] >> shift)) {
			swap(a[i], a[rev[i] >> shift]);
		}
	}
	for(int k = 1; k < n; k <<= 1) {
		for(int i = 0; i < n; i += 2 * k) {
			for(int j = 0; j < k; j++) {
				num z = a[i+j+k] * roots[j+k];
				a[i+j+k] = a[i+j] - z;
				a[i+j] = a[i+j] + z;
			}
		}
	}
}

vector<num> fa, fb;
vector<ll> multiply(vector<ll> &a, vector<ll> &b) {
	int need = a.size() + b.size() - 1;
	int nbase = 0;
	while((1 << nbase) < need) nbase++;
	ensure_base(nbase);
	int sz = 1 << nbase;
	if(sz > (int) fa.size()) {
		fa.resize(sz);
	}
	for(int i = 0; i < sz; i++) {
		ll x = (i < (int) a.size() ? a[i] : 0);
		ll y = (i < (int) b.size() ? b[i] : 0);
		fa[i] = num(x, y);
	}
	fft(fa, sz);
	num r(0, -0.25 / sz);
	for(int i = 0; i <= (sz >> 1); i++) {
		int j = (sz - i) & (sz - 1);
		num z = (fa[j] * fa[j] - conj(fa[i] * fa[i])) * r;
		if(i != j) {
			fa[j] = (fa[i] * fa[i] - conj(fa[j] * fa[j])) * r;
		}
		fa[i] = z;
	}
	fft(fa, sz);
	vector<ll> res(need);
	for(int i = 0; i < need; i++) {
		res[i] = (ll)(fa[i].x+0.5);
	}
	return res;
}

int main(){
	int N;
	cin >> N;
	vector<ll> occAB(2*U+5);
	vector<ll> occC(2*U+5);
	unordered_map<ll,ll> cnt;
	ll max_x = -100000;
	ll min_x = 100000;
	for(int i = 0; i < N; i++){
		ll tmp;
		cin >> tmp;
		occAB[tmp+U] += 1;
		occC[-tmp+U] += 1;
		max_x = max(tmp, max_x);
		min_x = min(tmp, min_x);
		cnt[tmp] += 1;
	}

	vector<ll>a(U*2+5);
	vector<ll>b(U*2+5);
	vector<ll>c(U*2+5);
	for(int i = 0; i < 2*U+5; i++){
		a[i] = b[i] = occAB[i];
		c[i] = occC[i];   
	}

	// use FFT to count a+U + b+U + -c+U = 3U
	vector<ll> mul = multiply(a,b);
	mul = multiply(mul, c);

	ll res = mul[3*U];

	// (x, x, 2x)
	ll dup1 = 0;
  vector<ll> keys;
  vector<ll> values;
	for(auto& kv : cnt){
    keys.push_back(kv.first);
    values.push_back(kv.second);
	}
  for(int i = 0; i < keys.size(); i++){
		dup1 += cnt[keys[i] * 2] * values[i];
  }

	// (x, 0, x), (0, x, x)
	ll dup2 = 2*cnt[0] * (N - 1);

	ll ans = res - dup1 - dup2;

	cout << ans << endl;

	return 0;
}

