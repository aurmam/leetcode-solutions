# -*- coding: utf-8 -*-
"""
@author: Aurimas M.
"""

class Solution:

    def first_duplicate(self, b):
        for idx, value in enumerate(b):
            if b[abs(b[idx]) - 1] < 0:
                return abs(b[idx])
            else:
                b[abs(b[idx]) - 1] = -b[abs(b[idx]) - 1]

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.first_duplicate([1,3,4,2,2]))
    print(sol.first_duplicate([3,1,3,4,2]))
    print(sol.first_duplicate([3,3,3,3,3]))


