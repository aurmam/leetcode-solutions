# -*- coding: utf-8 -*-
"""
@author: Aurimas M.
"""

class Solution:

    def max_area(self, height):

        right = len(height) - 1
        left = 0
        result = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            result = max(result, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right += -1

        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    print(sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.max_area([1, 1]))
    print(sol.max_area([4, 3, 2, 1, 4]))
    print(sol.max_area([1, 2, 1]))