class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
            
        hight = len(nums) - 1

        while low < hight:            
            
            mid = (low + hight) // 2
            
            if nums[mid] < nums[hight]:
                hight = mid
            else:
                low = mid + 1
        
        return nums[low]
        # return min(nums)
    
def main():
    solution = Solution()
    # nums = [3,4,5,1,2] # -> 1
    # nums = [4,5,6,7,0,1,2] # -> 0
    nums = [11,13,15,17] # -> 11
    print(nums)
    
    print(solution.findMin(nums))
    
if __name__ == "__main__":
    main()