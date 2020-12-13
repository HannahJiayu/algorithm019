class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False
        up, down = 0, len(matrix) - 1
        row = -1
        while up <= down:
            mid = up + (down - up) // 2 
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] <= target:
                up = mid + 1
            elif matrix[mid][0] >= target:
                down = mid - 1
        if row == -1:
            return False
        else:
            l, r = 0, len(matrix[row])
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
#独立做出来的哦！