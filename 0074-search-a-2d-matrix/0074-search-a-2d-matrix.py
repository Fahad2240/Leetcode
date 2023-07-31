class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            for scan in item:
                if scan==target:
                    return True
        return False