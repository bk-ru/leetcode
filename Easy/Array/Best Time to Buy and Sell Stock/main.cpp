#include <iostream>
#include <vector>

class Solution {
    public:
        int maxProfit(std::vector<int>& prices) {
            int buy = float('inf');
            int profit = 0;

            for (int price : prices) {
                if ((price - buy > profit))
                    profit = price - buy;
                if (buy > price)
                    buy = price;
            }

            return profit;
        }
    };

int main(void) {
    Solution solution;
    std::vector<int> prices = {7,1,5,3,6,4};

    std::cout << solution.maxProfit(prices);

}