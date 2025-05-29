class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a = 1
        b = 0
        tmp = 0
        
        while (n != 0):
            n -= 1
            tmp = a
            a = b + a
            b = tmp
            
        return a
       
def main():
    solution = Solution()
    n = 3
    print(solution.climbStairs(n))

if __name__ == "__main__":
    main()