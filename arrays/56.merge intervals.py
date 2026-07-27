from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge all overlapping intervals into one.
        
        Example:
            Input:  [[1,3],[2,6],[8,10],[15,18]]
            Output: [[1,6],[8,10],[15,18]]
        """
        
        merged = []
        
        # Step 1: Sort intervals by their start value (and end as tie-breaker).
        # This guarantees that any interval which could overlap with the
        # current one will always come right after it in the list.
        intervals.sort()
        
        # Step 2: Walk through each interval in sorted order
        for i in intervals:
            
            # Case 1: merged is empty (first interval)
            #      OR the last merged interval ends BEFORE this one starts
            #         -> there's a gap, so no overlap
            # In both cases, this interval starts a new group.
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            
            # Case 2: the current interval overlaps (or touches) the last
            # interval in merged. Extend its end to cover both.
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        
        return merged


# --- quick test ---
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    # Expected: [[1,6],[8,10],[15,18]]
    
    print(sol.merge([[1,4],[4,5]]))
    # Expected: [[1,5]]  (touching intervals count as overlapping)
    
    print(sol.merge([[1,4],[0,4]]))
    # Expected: [[0,4]]
    
    print(sol.merge([[1,4],[2,3]]))
    # Expected: [[1,4]]  (fully contained interval)