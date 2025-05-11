#include <iostream>
#include <vector>

class Solution 
{
public:
    int maxProduct(std::vector<int>& nums) {
        int result = nums[0];
        int minMult = 1, maxMult = 1;
        int tmp;

        for (int num : nums) {
            if (num == 0) {
                minMult = 1, maxMult = 1;
                result = std::max(result, num);
                continue;
            }
            tmp = maxMult * num;
            maxMult = std::max(maxMult * num, std::max(minMult * num, num));
            minMult = std::min(tmp, std::min(minMult * num, num));
            result = std::max(maxMult, result);
        }

        return result;
    }
};

int main(void)
{
    Solution solution;
    std::vector<int> nums = {-2, 0, -1};

    std::cout << solution.maxProduct(nums);
}