#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int size;
    std::cin >> size;
    
    std::vector<int> sequence(size);
    for(int i = 0; i < size; i++) {
        std::cin >> sequence[i];
    }
    
    std::vector<int> distinctCount(size + 1, 0);
    std::vector<int> previousSeen(size + 1, 0);
    int uniqueElements = 0;

    for(int i = 1; i <= size; i++) {
        int currentNum = sequence[i - 1];
        if(previousSeen[currentNum] == 0) {
            uniqueElements++;
        }
        previousSeen[currentNum] = i;
        distinctCount[i] = uniqueElements;
    }

    std::vector<std::vector<int>> occurrences(size + 1);
    for(int i = 1; i <= size; i++) {
        int currentNum = sequence[i - 1];
        occurrences[currentNum].push_back(i);
    }
    
    long long result = 0;
    for(int num = 1; num <= size; num++) {
        if(occurrences[num].size() >= 2) {
            int secondToLast = occurrences[num][occurrences[num].size() - 2];
            if(secondToLast > 1) {
                int distinctBefore = distinctCount[secondToLast - 1];
                if(occurrences[num][0] <= secondToLast - 1) {
                    distinctBefore--;
                }
                
                if(distinctBefore > 0) {
                    result += distinctBefore;
                }
            }
        }
    }
    
    std::cout << result << std::endl;
    
    return 0;
}