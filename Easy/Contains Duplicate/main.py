class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums_map = {}
        # for i in nums:
        #     if i in nums_map:
        #         return True
        #     nums_map[i] = None
        # return False
        return (len(set(nums)) < len(nums))
        
def main():
    solution = Solution()
    nums = [1,2,3,4]
    
    print(solution.containsDuplicate(nums))    
    
if __name__ == "__main__":
    main()