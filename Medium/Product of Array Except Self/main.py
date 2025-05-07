class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        mult = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mult *= num
        for num in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                res.append(0 if num != 0 else mult)
            else:
                res.append(mult // num)
        return res        
        
def main():
    solution = Solution()
    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums))
    
    
if __name__ == "__main__":
    main()