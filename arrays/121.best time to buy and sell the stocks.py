from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy day (left pointer), r = sell day (right pointer)
        l, r = 0, 0
        maxp = 0  # ab tak ka best profit store karega
        n = len(prices)

        while r < n:
            # Step 1: agar aaj ka price left(buy) wale price se zyada hai,
            # toh profit calculate karo
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]

                # Step 2: agar ye profit ab tak ke best se zyada hai, update karo
                if maxp < profit:
                    maxp = profit
            else:
                # Step 3: agar price gir gaya (prices[r] <= prices[l]),
                # matlab ye purana "l" ab sabse sasta nahi raha
                # isliye left pointer ko yahin move kardo (naya potential buy point)
                l = r

            # Step 4: har iteration mein right pointer aage badhao
            r += 1

        return maxp


# ---------------- Test cases ----------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5 (buy@1, sell@6)
    print(sol.maxProfit([7, 6, 4, 3, 1]))       # Expected: 0 (prices only fall)