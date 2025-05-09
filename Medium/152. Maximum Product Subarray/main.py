import numpy as np

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = max(nums)
        curMin = curMax = 1
        
        for num in nums:
            if num == 0:
                curMin = curMax = 1
                continue
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            result = max(result, curMax)
        return result
        
def main():
    # [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, -10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    # [1, 2, -3, 4, 2]
    # [-1, -2, -3, -4]  
    solution = Solution()
    # nums = np.random.randint(-10, 10, size=6)
    nums = [1, 2, -3, 4, 2]
    print(nums)
    
    print(solution.maxProduct(nums)) # -> 6
    
if __name__ == "__main__":
    main()