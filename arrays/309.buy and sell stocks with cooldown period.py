def maxProfit(prices):
    dp = {}  # memoization dictionary: key = (i, buying), value = max profit from that state

    def dfs(i, buying):
        # Base case: agar prices khatam ho gaye, toh koi profit possible nahi
        if i >= len(prices):
            return 0

        # Step 1: agar ye state pehle solve kar chuke hain, seedha return karo
        if (i, buying) in dp:
            return dp[(i, buying)]

        # Option 1: aaj kuch mat karo, agle din try karo (cooldown / skip)
        cooldown = dfs(i + 1, buying)

        if buying:
            # Agar hum "buying" state mein hain, toh do choices hain:
            # a) aaj stock buy karlo -> price minus ho jayega, aur ab "selling" state mein chale jao
            buy = dfs(i + 1, not buying) - prices[i]

            # Step 2: dono options mein se best wala store karo (buy vs cooldown)
            dp[(i, buying)] = max(buy, cooldown)

        else:
            # Agar hum "selling" state mein hain (matlab already stock hold kar rahe hain), toh:
            # a) aaj sell kardo -> price add ho jayega
            #    sell ke baad cooldown compulsory hai, isliye seedha i+2 pe jump karo (1 din skip)
            sell = dfs(i + 2, not buying) + prices[i]

            # Step 3: dono options mein se best wala store karo (sell vs cooldown)
            dp[(i, buying)] = max(sell, cooldown)

        return dp[(i, buying)]

    # Start: index 0 se, aur "buying" state mein (kyunki shuru mein koi stock hold nahi kar rahe)
    return dfs(0, True)


# ---------------- Test cases ----------------
if __name__ == "__main__":
    print(maxProfit([1, 2, 3, 0, 2]))   # Expected: 3
    print(maxProfit([1]))                # Expected: 0
    print(maxProfit([1, 2, 4]))           # Expected: 3