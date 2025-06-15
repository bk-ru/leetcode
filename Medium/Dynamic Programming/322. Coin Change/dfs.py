class Solution:    
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        visited = {}
        
        def dfs(visit):
            if visit < 0:
                return float('inf')
            if visit == 0:
                return 0
            if visit in visited:
                return visited[visit]
            
            min_iter = float('inf')
            for coin in coins:
                result = dfs(visit - coin)
                if result != float('inf'):
                    min_iter = min(min_iter, result + 1)
            
            visited[visit] = min_iter
            return min_iter
        
        min_iter = dfs(amount)
        
        return min_iter if min_iter != float('inf') else -1
        
    
def main():
    solution = Solution()
    
    coins = [1, 2, 5]
    amount = 11
    
    print(solution.coinChange(coins, amount))
    
if __name__ == "__main__":
    main()