#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int INF = 2147483647;
const long long INFL = 9223372036854775807LL;
const double EPSILON = 0.00000001;
const long long MOD = 1000000007;

int grid[85][85];
int best[85][85];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

struct state 
{
    int i,j,val;
};
bool operator < (const state& a, const state& b) {
    return a.val > b.val;
}

int32_t main()
{
    #ifdef DEBUG
    //freopen("A.txt","r",stdin);
    //freopen("","w",stdout);
    #endif

    int n = 80;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (j)
                scanf(",%d",&grid[i][j]);
            else 
                scanf("%d",&grid[i][j]);                
            best[i][j] = INF;
        }
    }
    
    priority_queue<state> pq;
    pq.push((state){0,0,grid[0][0]});
    best[0][0] = grid[0][0];
    
    while (not pq.empty()) {
        state top = pq.top(); 
        pq.pop();
        int i=top.i, j=top.j, val=top.val;
        if (val > best[i][j])
            continue;
        if (i == n-1 and j == n-1) {
            cout<<val<<endl;
            break;
        }
        for (int k=0; k<4; k++) {
            int ii = i+dy[k], jj = j+dx[k];
            if (0 <= ii and ii < n and 0 <= jj and jj < n) {
                int next_val = val + grid[ii][jj];
                if (next_val < best[ii][jj]) {
                    pq.push((state){ii,jj,next_val});
                    best[ii][jj] = next_val;
                }
            }
        }
    }
    return 0;
}
