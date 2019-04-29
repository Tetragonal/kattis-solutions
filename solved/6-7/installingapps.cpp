#include<bits/stdc++.h>
using namespace std;
const int maxn = 505, maxc = 1e4+5;

struct A{
    int d, s, i;
}apps[maxn];

struct B{
    int n, idx, y,x;
}dp[maxn][maxc];
int ans[maxn];

bool cmp(A x, A y) {
    if (max(x.s,x.d)+y.s == max(y.s,y.d)+x.s)
        return x.s < y.s;
    return (max(x.s,x.d)+y.s > max(y.s,y.d)+x.s);
}

int main() {
    //freopen("in.txt", "r", stdin);
    int n, c;
    cin>>n>>c;

    for (int i = 0; i < n; i++) {
        cin>>apps[i].d>>apps[i].s;
        apps[i].i = i+1;
    }
    sort(apps, apps+n, cmp);
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++) {
        for (int j = c; j >= 0; j--) {
            if (j >= apps[i-1].s && c - j >= apps[i-1].d - apps[i-1].s) {
                if (dp[i-1][j-apps[i-1].s].n + 1 > dp[i][j].n) {
                    dp[i][j].n = dp[i-1][j-apps[i-1].s].n + 1;
                    dp[i][j].idx = apps[i-1].i;
                    dp[i][j].x = j-apps[i-1].s;
                    dp[i][j].y = i-1;
                }
            }
            if (dp[i][j].n < dp[i-1][j].n) {
            //if (dp[i][j].n == 0) {
                dp[i][j].n = dp[i-1][j].n;
                dp[i][j].idx = dp[i-1][j].idx;
                dp[i][j].y = dp[i-1][j].y;
                dp[i][j].x = dp[i-1][j].x;
            }
        }
    }
    int tmp_x = n, opt = 0;
    int tmp_y = n;
    for (int i = 0; i <= c; i++) {
        if (dp[n][i].n > opt) {
            opt = dp[n][i].n;
            tmp_x = i;
        }
    }

    /*
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= c; j++)
            cout<<dp[i][j].n<<' '<<dp[i][j].idx<<' '<<dp[i][j].x<<' '<<dp[i][j].y<<"        ";
        cout<<endl;
    }
    */

    cout<<opt<<endl;
    if (opt > 0) {
        int cnt = opt;
        while (dp[tmp_y][tmp_x].idx != 0) {
            //while (dp[j][tmp].idx == 0) j--;
            ans[--cnt] = dp[tmp_y][tmp_x].idx;
            int tmp_x_2 = dp[tmp_y][tmp_x].x;
            int tmp_y_2 = dp[tmp_y][tmp_x].y;
            tmp_y = tmp_y_2;
            tmp_x = tmp_x_2;
        }
        cout<<ans[0];
        for (int i = 1; i < opt; i++)
            cout<<' '<<ans[i];
        cout<<endl;
    }
}
