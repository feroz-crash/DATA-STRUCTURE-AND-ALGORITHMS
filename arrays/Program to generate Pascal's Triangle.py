from typing import List
# Solution class to find the (r, c) element of Pascal's Triangle
class Solution:
    # Function to compute binomial coefficient (nCr)
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result


# Main code to test the solution
if __name__ == "__main__":
    sol = Solution()
    numrows=5  # Row index (0-based)
    print(sol.generate(numrows))