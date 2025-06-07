#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <sstream>

int solve_single_case(int grid_size, int shift_x, int shift_y, const std::vector<std::string>& pixel_grid) {
    std::vector<std::vector<bool>> is_marked(grid_size, std::vector<bool>(grid_size, false));
    std::vector<std::vector<bool>> is_shifter(grid_size, std::vector<bool>(grid_size, false));
    int marked_count = 0;

    auto mark_pixel = [&](int row, int col) {
        if (!is_marked[row][col]) {
            is_marked[row][col] = true;
            marked_count++;
        }
    };

    for (int row = 0; row < grid_size; ++row) {
        for (int col = 0; col < grid_size; ++col) {
            if (pixel_grid[row][col] == 'B') {
                if (row - shift_y < 0 || col - shift_x < 0) {
                    return -1;
                }
                int shifter_row = row - shift_y;
                int shifter_col = col - shift_x;
                if (is_shifter[shifter_row][shifter_col]) {
                    return -1;
                }
                is_shifter[shifter_row][shifter_col] = true;
                mark_pixel(row, col);
                mark_pixel(shifter_row, shifter_col);
            }
        }
    }

    // Process gray pixels
    for (int row = 0; row < grid_size; ++row) {
        for (int col = 0; col < grid_size; ++col) {
            if (pixel_grid[row][col] == 'G') {
                int cost_current = is_marked[row][col] ? 0 : 1;
                double cost_shifter = std::numeric_limits<double>::infinity();
                
                if (row - shift_y >= 0 && col - shift_x >= 0) {
                    int shifter_row = row - shift_y;
                    int shifter_col = col - shift_x;
                    if (!is_shifter[shifter_row][shifter_col]) {
                        cost_shifter = is_marked[shifter_row][shifter_col] ? 0 : 1;
                    }
                }

                if (cost_current <= cost_shifter) {
                    if (cost_current == 1) {
                        mark_pixel(row, col);
                    }
                } else {
                    int shifter_row = row - shift_y;
                    int shifter_col = col - shift_x;
                    mark_pixel(shifter_row, shifter_col);
                    is_shifter[shifter_row][shifter_col] = true;
                }

                if (cost_current == std::numeric_limits<double>::infinity() && 
                    cost_shifter == std::numeric_limits<double>::infinity()) {
                    return -1;
                }
            }
        }
    }

    for (int row = 0; row < grid_size; ++row) {
        for (int col = 0; col < grid_size; ++col) {
            if (pixel_grid[row][col] == 'W') {
                if (is_marked[row][col]) {
                    return -1;
                }
                int shifter_row = row - shift_y;
                int shifter_col = col - shift_x;
                if (0 <= shifter_row && shifter_row < grid_size && 
                    0 <= shifter_col && shifter_col < grid_size) {
                    if (is_marked[shifter_row][shifter_col] && 
                        is_shifter[shifter_row][shifter_col]) {
                        return -1;
                    }
                }
            }
        }
    }

    return marked_count;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int num_test_cases;
    std::cin >> num_test_cases;

    std::vector<int> results;
    for (int i = 0; i < num_test_cases; ++i) {
        int grid_size, shift_x, shift_y;
        std::cin >> grid_size >> shift_x >> shift_y;

        std::vector<std::string> pixel_grid(grid_size);
        for (int j = 0; j < grid_size; ++j) {
            std::cin >> pixel_grid[j];
        }

        results.push_back(solve_single_case(grid_size, shift_x, shift_y, pixel_grid));
    }

    for (const auto& result : results) {
        std::cout << result << '\n';
    }

    return 0;
}