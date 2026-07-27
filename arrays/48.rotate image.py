from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given n x n matrix by 90 degrees clockwise, in-place.
        
        Approach: Layer by layer rotation.
        Think of the matrix as a set of concentric square "rings" (layers).
        For each layer, we rotate elements 4 at a time (a 4-way swap):
            top-left -> top-right -> bottom-right -> bottom-left -> top-left
        We do this for every group of 4 cells in that layer, then move
        one layer inward and repeat.
        """
        
        # l = left boundary, r = right boundary of the current layer (ring)
        l, r = 0, len(matrix) - 1
        
        # Keep shrinking the ring inward until l meets/crosses r
        while l < r:
            
            # For each layer, there are (r - l) elements to rotate along one edge
            # (the last element of each edge is handled by the next group, hence r-l not r-l+1)
            for i in range(r - l):
                
                # Fix the corners of the current layer for this iteration
                top, bottom = l, r
                
                # 1. Save top-left element (this will be overwritten first)
                topleft = matrix[top][l + i]
                
                # 2. Move bottom-left element -> top-left
                #    (bottom row, moving up along the left column)
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # 3. Move bottom-right element -> bottom-left
                #    (moving along the bottom row from right to left)
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # 4. Move top-right element -> bottom-right
                #    (moving down along the right column)
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # 5. Place the saved top-left value -> top-right
                #    (completes the 4-way cyclic rotation)
                matrix[top + i][r] = topleft
            
            # Shrink the ring: move to the next inner layer
            r -= 1
            l += 1