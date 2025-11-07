#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T; 
    if(!(cin >> T)) return 0;
    while (T--) {
        int n; long long kmax;a
        cin >> n >> kmax;
        string s, t; 
        cin >> s >> t;

        if (s[0] != t[0]) { cout << -1 << '\n'; continue; }

        vector<int> last(26, -1);
        vector<int> p(n, -1);
        int prev = 0;

        long long K = 0;

        for (int i = 0; i < n; ++i) {
            last[s[i]-'a'] = i;
            int j = last[t[i]-'a'];
            if (j == -1 || j < prev) {
                K = kmax + 1;
                break;
            }
            p[i] = j;
            prev = j;
            K = max(K, (long long)(i - j));
        }

        if (K > kmax) { cout << -1 << '\n'; continue; }

        vector<int> R(n);
        iota(R.begin(), R.end(), 0);
        for (int i = 0; i < n; ++i) R[p[i]] = max(R[p[i]], i);

        cout << K << '\n';
        string cur = s;
        for (long long r = 1; r <= K; ++r) {
            string nxt = cur;
            for (int j = 0; j < n; ++j) {
                int pos = j + (int)r;
                if (pos < n && pos <= R[j]) {
                    nxt[pos] = cur[pos - 1];
                }
            }
            cur = move(nxt);
            cout << cur << '\n';
        }
    }
    return 0;
}