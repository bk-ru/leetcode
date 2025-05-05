#include <iostream>
#include <vector>
#include <map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::map<int, int> num_map;
        std::vector<int> result = {};

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (num_map.count(diff) > 0) {
                result.push_back(num_map[diff]);
                result.push_back(i);
                break;
            }
            num_map[nums[i]] = i;
        }
        return result;
    }
};

int main(void) {
    Solution solution;
    std::vector<int> nums = {2,4,5,6};
    int target = 6;
    
    std::vector<int> result = solution.twoSum(nums, target);
    
    for (auto x : result) {
        std::cout << x << " ";
    }
}