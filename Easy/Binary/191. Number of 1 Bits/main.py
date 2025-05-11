# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
        
#         while n > 0:
#             if n & 1 == 1:
#                 count += 1
#             n = n >> 1
#         return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        tmp = n
        count = 0
        
        while True:
            count += tmp % 2
            tmp = tmp // 2
            if tmp == 0:
                return count

def main():
    solution = Solution()
    print(solution.hammingWeight(11))
    
if __name__ == "__main__":
    main()