from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy day (left pointer), r = sell day (right pointer)
        buy,sell= 0, 0
        maxp = 0  # ab tak ka best profit store karega
        n = len(prices)

        while sell < n:
            # Step 1: agar aaj ka price left(buy) wale price se zyada hai,
            # toh profit calculate karo
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]

                # Step 2: agar ye profit ab tak ke best se zyada hai, update karo
                if maxp < profit:
                    maxp = profit
            else:
                # Step 3: agar price gir gaya (prices[sell] <= prices[buy]),
                # matlab ye purana "buy" ab sabse sasta nahi raha
                # isliye buy pointer ko yahin move kardo (naya potential buy point)
                buy = sell

            # Step 4: har iteration mein right pointer aage badhao
            sell += 1

        return maxp


# ---------------- Test cases ----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5 (buy@1, sell@6)
    print(sol.maxProfit([7, 6, 4, 3, 1]))       # Expected: 0 (prices only fall)