#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;

    vector<int> arrayA(N), arrayB(N);
    for(int i = 0; i < N; i++){
        cin >> arrayA[i];
    }
    for(int i = 0; i < N; i++){
        cin >> arrayB[i];
    }

    int initialMatches = 0;
    for(int i = 0; i < N; i++){
        if(arrayA[i] == arrayB[i]) {
            initialMatches++;
        }
    }

    vector<long long> resultCounts(N+1, 0LL);
    for(int currentSum = 2; currentSum <= 2*N; currentSum++) {
        vector<int> prefixSums(N+1, 0);
        for(int currentIndex = 1; currentIndex <= N; currentIndex++) {
            int changeInMatch = 0;
            int pairedIndex = currentSum - currentIndex;  
            if(pairedIndex >= 1 && pairedIndex <= N) {
                if(arrayA[pairedIndex-1] == arrayB[currentIndex-1]) {
                    changeInMatch += 1;
                }
            }
            if(arrayA[currentIndex-1] == arrayB[currentIndex-1]) {
                changeInMatch -= 1;
            }
            prefixSums[currentIndex] = prefixSums[currentIndex-1] + changeInMatch;
        }

        int startLeft = max(1, currentSum - N);
        int endLeft = min(currentSum - 1, N);
        for(int left = startLeft; left <= endLeft; left++) {
            int right = currentSum - left;
            if(left > right) {
                continue; 
            }
            long long totalMatches = (long long)initialMatches + (prefixSums[right] - prefixSums[left-1]);
            resultCounts[totalMatches]++;
        }
    }
    for(int count = 0; count <= N; count++) {
        cout << resultCounts[count] << "\n";
    }

    return 0;
}