class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_array = 0
        iter1 = 0
        iter2 = 0
        flag = 0
        
        for num in nums:
            if num == 1:
                iter1 += 1
                iter2 += 1
                max_array = max(iter1, iter2, max_array)
            else:
                flag += 1
                iter2 = iter1
                iter1 = 0
        return max_array if flag != 0 else max_array - 1
        
def main():
    solution = Solution()
    nums  = [1,1,1]
    
    print(solution.longestSubarray(nums))
    
if __name__ == "__main__":
    main()