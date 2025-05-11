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