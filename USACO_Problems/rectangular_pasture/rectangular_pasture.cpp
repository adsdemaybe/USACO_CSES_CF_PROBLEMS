#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

class Cow {
public:
    int x, y;
    Cow(int x, int y) : x(x), y(y) {}
};

// Helper function for debugging
void printCow(const Cow &cow) {
    cout << "(" << cow.x << ", " << cow.y << ")";
}

int main() {
    int n;
    cin >> n;

    vector<Cow> cows;
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        cows.emplace_back(x, y);
    }

    // Compress Cow Coords
    sort(cows.begin(), cows.end(), [](const Cow &a, const Cow &b) {
        return a.x < b.x;
    });
    int ind = 1;
    for (auto &cow : cows) {
        cow.x = ind++;
    }
    int max_x = ind;

    sort(cows.begin(), cows.end(), [](const Cow &a, const Cow &b) {
        return a.y < b.y;
    });
    ind = 1;
    for (auto &cow : cows) {
        cow.y = ind++;
    }
    int max_y = ind;

    vector<vector<int>> locs(max_y, vector<int>(max_x, 0));
    for (const auto &cow : cows) {
        locs[cow.y][cow.x] = 1;
    }

    // Make prefix sum
    vector<vector<int>> pref_sum = locs;
    for (int i = 1; i < max_y; ++i) {
        for (int j = 1; j < max_x; ++j) {
            pref_sum[i][j] += pref_sum[i - 1][j] + pref_sum[i][j - 1] - pref_sum[i - 1][j - 1];
        }
    }

    // Count Cows Above and Below
    sort(cows.begin(), cows.end(), [](const Cow &a, const Cow &b) {
        return a.x < b.x;
    });

    long long count = n + 1;
    for (int anchor_ind = 0; anchor_ind < n; ++anchor_ind) {
        for (int target_ind = anchor_ind + 1; target_ind < n; ++target_ind) {
            int left_x = cows[anchor_ind].x;
            int right_x = cows[target_ind].x;
            int bott_y = max(cows[anchor_ind].y, cows[target_ind].y);
            int top_y = min(cows[anchor_ind].y, cows[target_ind].y);

            int top_cows_count = pref_sum[top_y][right_x] - pref_sum[top_y][left_x - 1];
            int bot_cows_count = pref_sum[max_y - 1][right_x] - pref_sum[max_y - 1][left_x - 1] - pref_sum[bott_y - 1][right_x] + pref_sum[bott_y - 1][left_x - 1];
            
            count += static_cast<long long>(top_cows_count) * bot_cows_count;
        }
    }

    cout << count << endl;

    return 0;
}