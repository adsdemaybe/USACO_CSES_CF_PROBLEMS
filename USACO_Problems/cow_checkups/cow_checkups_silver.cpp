#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Counts how many sub-intervals [l,r] (with 1 <= l <= r <= N)
 * satisfy:
 *   l <= i <= r, l <= j <= r,  (so i, j in [l,r])
 *   and l + r = s.
 *
 * If s < 2 or s > 2*N, clearly no solutions. Otherwise:
 *   l = L .. R, and r = s - l.
 *   We need l <= i and r >= i  => l <= i <= r => l <= i <= s-l
 *   Similarly l <= j <= s-l
 *   And also 1 <= l <= r <= N.
 *
 * We can show that l must be at least max(1, s-N),
 * and at most min( floor(s/2), i, s-j ).
 * So the number of valid l is # of integers in [L, R] where
 *   L = max(1, s-N),
 *   R = min(floor(s/2), i, s - j).
 */
long long H(int s, int i, int j, int N) {
    // lower bound for l
    int L = max(1, s - N);
    // upper bound for l
    int half_s = s / 2;  // floor division
    int R = min({half_s, i, s - j});
    if (R < L) return 0LL;
    return (long long)(R - L + 1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> a(N+1), b(N+1);
    for(int i = 1; i <= N; i++) {
        cin >> a[i];
    }
    for(int i = 1; i <= N; i++) {
        cin >> b[i];
    }

    // 1) Calculate baseMatches (positions i where a[i] == b[i]).
    long long baseMatches = 0;
    for (int i = 1; i <= N; i++){
        if(a[i] == b[i]) {
            baseMatches++;
        }
    }

    // 2) Calculate lostSum = sum of i*(N-i+1) over all i s.t. a[i] == b[i].
    long long lostSum = 0;
    for(int i = 1; i <= N; i++){
        if(a[i] == b[i]){
            lostSum += 1LL * i * (N - i + 1);
        }
    }

    // 3) Calculate gainedSum by grouping positions by species.
    // posA[x] = list of positions j where a[j] == x
    // posB[x] = list of positions i where b[i] == x
    vector<vector<int>> posA(N+1), posB(N+1);
    for(int j = 1; j <= N; j++){
        posA[a[j]].push_back(j);
    }
    for(int i = 1; i <= N; i++){
        posB[b[i]].push_back(i);
    }

    // For each species x, consider all i in posB[x] and j in posA[x].
    // If a[j] = x and b[i] = x, then reversing some sub-interval [l,r]
    // can place the cow originally at j into position i.
    // The number of such [l,r] is H(i+j, i, j, N).
    long long gainedSum = 0;
    for(int x = 1; x <= N; x++){
        // For all i, j where b[i] == x and a[j] == x, add H(i+j, i, j)
        for(int iPos : posB[x]){
            for(int jPos : posA[x]){
                int s = iPos + jPos;
                // Quick check to skip if s out of possible range
                if (s < 2 || s > 2*N) continue;
                gainedSum += H(s, iPos, jPos, N);
            }
        }
    }

    // Combine everything:
    // totalBase = baseMatches * number_of_subintervals
    long long totalBase = baseMatches * (long long)N * (N + 1) / 2;
    long long answer = totalBase - lostSum + gainedSum;

    cout << answer << "\n";
    return 0;
}