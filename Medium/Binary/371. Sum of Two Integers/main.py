class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF # 32 bit
        
        while (b != 0):
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask
            
        return a if a < max_int else ~(a ^ mask)
    
def main():
    solutin = Solution()
    a, b = -1, 2
    print(solutin.getSum(a, b))
    
if __name__ == "__main__":
    main()