from bisect import bisect_right


class Solution:
    # @param A : list of list of integers
    # @return an integer
    # def findMedian(self, A):
    #     temp = []
    #     for i in range(len(A)):
    #         for j in range(len(A[0])):
    #             temp.append(A[i][j])
    #     temp.sort()
    #     mid = len(temp)//2
    #     if len(temp) % 2 != 0:
    #         return temp[mid]
    #     return [temp[mid - 1], temp[mid]]
    def binSearch(self, matrix, min_el, max_el, cntElBeforeMed):
        start = min_el
        end = max_el
        while start < end:
            mid = start + ((end - start) // 2)
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt > cntElBeforeMed:
                end = mid
            else:
                start = mid + 1

        return start

    def getMinMax(self, matrix):
        min_el = float('inf')
        max_el = float('-inf')
        for row in matrix:
            if min_el > row[0]:
                min_el = row[0]
            if max_el < row[-1]:
                max_el = row[-1]

        return min_el, max_el

    def findMedian(self, A):
        matrix = A
        rn = len(matrix)
        cn = len(matrix[0])
        cntElBeforeMed = (rn * cn) // 2
        min_el, max_el = self.getMinMax(matrix)
        return self.binSearch(matrix, min_el, max_el, cntElBeforeMed)


test = Solution()
print(test.findMedian([[1, 3, 5],
                       [2, 6, 9],
                       [3, 6, 9]]))
