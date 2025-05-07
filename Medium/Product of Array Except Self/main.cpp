#include <iostream>
#include <vector>

class Solution {
    public:
        std::vector<int> productExceptSelf(std::vector<int>& nums) {
            std::vector<int> result = {};

            int mult = 1;
            for (int i : nums) {
                result.push_back(mult);
                mult *= i;
            }

            mult = 1;
            for (int i = nums.size() - 1; i >= 0; i--) {
                result[i] *= mult;
                mult *= nums[i];
            }

            return result;
        }
    };

int main(void) {
    std::vector<int> nums = {1,2,3,4};

    Solution solution;

    for (int i : solution.productExceptSelf(nums)) {
        std::cout << i << ", ";
    }
}