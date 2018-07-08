#include <bits/stdc++.h>

using namespace std;

vector<int> sol[750001];
int cnt[750001];

int main()
{    
    int ans = 0;
    int MAX = 750000;
    memset(cnt,0,sizeof(cnt));
    for (int l=0; l<=MAX; l++)
        sol[l] = vector<int>({-1,-1,-1}); //no solution
    int a,b,c,n,m;
    
    for (int l=3; l<=MAX; l++) {
        if (cnt[l] == 2)
            continue;
        
        int low = ceil(sqrt(l)/sqrt(2));
        for (m=low; m*m<l; m++) {
            if (2*m*m > l and l%m == 0) {
                n = l/m - m;
                a = m*m - n*n;
                b = 2*m*n;
                c = m*m + n*n;
                if (a > b)
                    swap(a,b);
                assert(b > a);
                assert(c > b);
                
                if (sol[l][0] == -1) {
                    sol[l][0] = a;
                    sol[l][1] = b;
                    sol[l][2] = c;
                    cnt[l] = 1;
                }
                else if (sol[l][0] != a) {
                    cnt[l] = 2;
                    break;
                }
            }
        }
        if (cnt[l] == 1) {
            ans++;
            for (int k=2; k*l<=MAX; k++) {
                int kl = k*l;
                if (sol[kl][0] == -1) {
                    cnt[kl] = 1;
                    sol[kl][0] = k*sol[l][0];
                    sol[kl][1] = k*sol[l][1];
                    sol[kl][2] = k*sol[l][2];
                }
                else if (sol[kl][0] != k*sol[l][0]) 
                    cnt[kl] = 2;
            }
        }
        else if (cnt[l] == 2) {
            for (int k=2; k*l<=MAX; k++) {
                cnt[k*l] = 2;
            }
        }
    }
    cout<<ans<<endl;

    return 0;
}
