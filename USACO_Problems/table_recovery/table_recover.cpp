#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <tuple>

using namespace std;

typedef unordered_map<int, int> CountMap;
typedef unordered_map<int, vector<int>> GroupMap;

void solve() {
    int N;
    cin >> N;

    vector<vector<int>> F(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> F[i][j];
        }
    }

    CountMap counts_S, counts_F;
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            counts_S[r + c]++;
        }
    }

    for (const auto& row : F) {
        for (int val : row) {
            counts_F[val]++;
        }
    }

    GroupMap freq_to_sums, freq_to_vals;
    for (int s = 2; s <= 2 * N; ++s) {
        freq_to_sums[counts_S[s]].push_back(s);
    }
    for (const auto& entry : counts_F) {
        freq_to_vals[entry.second].push_back(entry.first);
    }

    for (auto& [freq, sums] : freq_to_sums) {
        sort(sums.begin(), sums.end());
    }
    for (auto& [freq, vals] : freq_to_vals) {
        sort(vals.begin(), vals.end());
    }

    vector<tuple<int, vector<int>, vector<int>>> grouped_x;
    for (const auto& [freq, x_list] : freq_to_sums) {
        grouped_x.emplace_back(freq, x_list, freq_to_vals[freq]);
    }

    vector<vector<int>> best_S_found;

    auto find_p_and_q = [&](const vector<vector<int>>& S, int N) -> pair<vector<int>, vector<int>> {
        for (int p0 = 1; p0 <= N; ++p0) {
            vector<int> q_candidate;
            bool valid = true;
            for (int c = 0; c < N; ++c) {
                int q = S[0][c] - p0;
                if (q < 1 || q > N) {
                    valid = false;
                    break;
                }
                q_candidate.push_back(q);
            }
            if (!valid || unordered_set<int>(q_candidate.begin(), q_candidate.end()).size() != N) continue;

            vector<int> p_candidate = {p0};
            for (int r = 1; r < N; ++r) {
                int p_r = S[r][0] - q_candidate[0];
                if (p_r < 1 || p_r > N) {
                    valid = false;
                    break;
                }
                p_candidate.push_back(p_r);
            }
            if (!valid || unordered_set<int>(p_candidate.begin(), p_candidate.end()).size() != N) continue;

            for (int r = 0; r < N; ++r) {
                for (int c = 0; c < N; ++c) {
                    if (S[r][c] != p_candidate[r] + q_candidate[c]) {
                        valid = false;
                        break;
                    }
                }
                if (!valid) break;
            }
            if (valid) return {p_candidate, q_candidate};
        }
        return {{}, {}};
    };

    function<void(int, unordered_map<int, int>&, unordered_set<int>&)> backtrack;
    backtrack = [&](int index, unordered_map<int, int>& current_phi, unordered_set<int>& used_y_set) {
        if (index == grouped_x.size()) {
            unordered_map<int, int> phi_inv;
            for (const auto& [k, v] : current_phi) {
                phi_inv[v] = k;
            }
            vector<vector<int>> S_reconstructed(N, vector<int>(N));
            for (int r = 0; r < N; ++r) {
                for (int c = 0; c < N; ++c) {
                    int y = F[r][c];
                    if (phi_inv.find(y) == phi_inv.end()) return;
                    S_reconstructed[r][c] = phi_inv[y];
                }
            }
            auto [p, q] = find_p_and_q(S_reconstructed, N);
            if (p.empty() || q.empty()) return;
            if (best_S_found.empty() || S_reconstructed < best_S_found) {
                best_S_found = S_reconstructed;
            }
            return;
        }

        auto [freq, x_list_sorted, y_list_sorted] = grouped_x[index];
        if (x_list_sorted.size() != y_list_sorted.size()) return;

        function<void(int, unordered_map<int, int>&, unordered_set<int>&)> assign_y_to_x;
        assign_y_to_x = [&](int pos, unordered_map<int, int>& temp_phi, unordered_set<int>& temp_used_y_set) {
            if (pos == x_list_sorted.size()) {
                backtrack(index + 1, temp_phi, temp_used_y_set);
                return;
            }

            int x = x_list_sorted[pos];
            for (int y : y_list_sorted) {
                if (temp_used_y_set.find(y) == temp_used_y_set.end()) {
                    temp_phi[x] = y;
                    temp_used_y_set.insert(y);
                    assign_y_to_x(pos + 1, temp_phi, temp_used_y_set);
                    temp_phi.erase(x);
                    temp_used_y_set.erase(y);
                }
            }
        };

        assign_y_to_x(0, current_phi, used_y_set);
    };

    unordered_map<int, int> current_phi;
    unordered_set<int> used_y_set;
    backtrack(0, current_phi, used_y_set);

    if (!best_S_found.empty()) {
        for (const auto& row : best_S_found) {
            for (size_t j = 0; j < row.size(); ++j) {
                if (j > 0) cout << " ";
                cout << row[j];
            }
            cout << endl;
        }
    }
}

int main() {
    solve();
    return 0;
}
