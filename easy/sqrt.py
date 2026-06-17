class Solution:
    def myExactSqrt(self, x: float) -> float:
        # Edge case: For numbers between 0 and 1 (like 0.25), the square root (0.5) 
        # is actually LARGER than the number itself. 
        # We ensure our right boundary is at least 1.0 to catch this.
        l, r = 0.0, max(x, 1.0)
        
        # We define a "precision" threshold. 
        # The loop stops when l and r are closer than 0.001 to each other.
        precision = 1e-3 
        
        while (r - l) > precision:
            # Normal float division
            m = l + (r - l) / 2.0
            
            if m**2 < x:
                # Midpoint squared is too small, shift the left boundary up to m
                l = m
            else:
                # Midpoint squared is too big, shift the right boundary down to m
                r = m
                
        # Once the window is tiny, returning the midpoint gives a highly accurate answer
        return l + (r - l) / 2.0

# --- How to test it ---
if __name__ == "__main__":
    solution = Solution()
    
    print("Exact sqrt of 4:", solution.myExactSqrt(4))       # Expected: ~2.0
    print("Exact sqrt of 8:", solution.myExactSqrt(8))       # Expected: ~2.82842
    print("Exact sqrt of 363:", solution.myExactSqrt(363))     # Expected: ~19.0526
    print("Exact sqrt of 0.25:", solution.myExactSqrt(0.25)) # Expected: ~0.5