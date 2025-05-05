class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        result = []

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hash_map:
                result.append(hash_map[diff])
                result.append(i)
                break
            
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i  
        return result

def main():
    solution = Solution()
    
    nums = [2, 7, 11, 17]
    target = 9
    
    result = solution.twoSum(nums, target)
    
    print(result)
    
if __name__ == "__main__":
    main()