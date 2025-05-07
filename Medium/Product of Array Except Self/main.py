class Solution(object):
    ### The implementation I came to
    
    # def productExceptSelf(self, nums):
    #     res = []
    #     mult = 1
    #     zero_count = 0
        
    #     for num in nums:
    #         if num == 0:
    #             zero_count += 1
    #         else:
    #             mult *= num
    #     for num in nums:
    #         if zero_count > 1:
    #             res.append(0)
    #         elif zero_count == 1:
    #             res.append(0 if num != 0 else mult)
    #         else:
    #             res.append(mult // num)
    #     return res
    
    def productExceptSelf(self, nums):
        res = []
        
        mult = 1
        for i in nums:
            res.append(mult)
            mult *= i
            
        mult = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * mult
            mult *= nums[i]
        return res

        
        
def main():
    solution = Solution()
    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums))
    
    
if __name__ == "__main__":
    main()