#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

class Solution {
    public:
        bool containsDuplicate(std::vector<int>& nums) {
            // std::map<int, int> my_map;
            
            // for (int i : nums) {
            //     if (my_map.count(i) > 0)
            //         return true;
            //     my_map[i] = i;
            // }
            // return false;

            sort(nums.begin(), nums.end());
            for (int i = 1; i < nums.size(); i++)
                if (nums[i] < nums[i - 1])
                    return true;
            return false;
        }
    };

int main(void) {
    Solution solution;
    std::vector<int> nums = {1,2,3,1};

    std::cout << solution.containsDuplicate(nums);
}