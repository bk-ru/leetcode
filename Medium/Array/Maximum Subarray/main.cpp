#include <iostream>
#include <vector>

class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int currentSum = 0;
        int maxSum = INT_MIN;

        for (int num : nums) {
            currentSum += num;
            if (currentSum > maxSum) 
                maxSum = currentSum;
            if (currentSum < 0)
                currentSum = 0;
        }
        return maxSum;
    }
};

int main(void) {
    Solution solution;
    std::vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};

    std::cout << solution.maxSubArray(nums);
}