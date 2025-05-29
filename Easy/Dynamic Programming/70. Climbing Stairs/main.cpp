#include <iostream>

class Solution 
{
public:
    int climbStairs(int n)
    {
        if (n <= 2)
            return n;
        
        int first = 1, second = 2;
        int tmp = 0;
        for (int i = 3; i < n + 1; i++) {
            tmp = second;
            second = first + second;
            first = tmp;
        }

        return second;
    }
};

int main(void) 
{
    Solution solution;
    int n = 5;
    std::cout << solution.climbStairs(n);    
}