# coding=utf-8

# 删除排序数组中的重复数字
# 核心思想是：在原地更改输入，且只更改特定的元素
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        k = 0
        for i in range(1, len(A)):
            if A[i] != A[k]:
                k += 1
                A[k] = A[i]

        del A[k + 1:len(A)]
        return len(A)

slover = Solution()
print slover.removeDuplicates([1,1,1,1,2,2,2,2,3,3,4])