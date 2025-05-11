#include <iostream>
#include <vector>

class Solution
{
public:
    int findMin(std::vector<int> nums)
    {
        int low = 0;
        int hight = nums.size() - 1;
        int mid;

        while (low < hight) {
            mid = (hight + low) / 2;

            if (nums[mid] < nums[hight])
                hight = mid;
            else
                low = mid + 1;
        }

        return nums[low];
    }
};

int main(void)
{
    Solution solution;
    std::vector<int> nums = {11, 13, 15, 17};

    std::cout << solution.findMin(nums);

}