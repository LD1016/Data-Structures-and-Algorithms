"""
Given a sorted array A containing N integers both positive and negative.
You need to create another array containing the squares of all the elements 
in A and return it in non-decreasing order.
Try to this in O(N) time.

Problem Constraints
1 <= N <= 105.
-103 <= A[i] <= 103

Input Format
First and only argument is an integer array A.

Output Format
Return a integer array as described in the problem above.

Example Input
Input 1:
 A = [-6, -3, -1, 2, 4, 5]
Input 2:
 A = [-5, -4, -2, 0, 1]

Example Output
Output 1:
 [1, 4, 9, 16, 25, 36]
Output 2:
 [0, 1, 4, 16, 25]
"""


class Solution:
    def solve(self, A):
        # negArr = []
        # posArr = []
        # for i in A:
        #     if i < 0:
        #         negArr.append(i)
        #     else:
        #         posArr.append(i)
        # negArr = [x*x for x in negArr]
        # posArr = [x*x for x in posArr]
        # # print(negArr, posArr)
        # return self.merge(self.mergeSort(negArr), self.mergeSort(posArr))
        i, j = 0, len(A) - 1
        result = []
        while i <= j:
            if A[i]*A[i] > A[j]*A[j]:
                result.append(A[i]*A[i])
                i += 1
            else:
                result.append(A[j]*A[j])
                j -= 1
        return result[::-1]

    def merge(self, left, right):
        result = []
        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] > right[rightIndex]:
                result.append(right[rightIndex])
                rightIndex += 1
            else:
                result.append(left[leftIndex])
                leftIndex += 1
        return result + left[leftIndex:] + right[rightIndex:]

    def mergeSort(self, arr):
        if (len(arr) == 1):
            return arr
        haft = len(arr) // 2
        left = arr[:haft]
        right = arr[haft:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))


test = Solution()
print(test.solve([-6, -3, -1, 2, 4, 5]))
print(test.solve([-855, -847, -747, -708, -701, -667, -666, -618, -609, -536, -533, -509, -500, -396, -336, -297, -284, -229, -173, -173, -132, -
                  38, -5, 35, 141, 169, 281, 322, 358, 421, 436, 447, 478, 538, 547, 644, 667, 673, 705, 711, 718, 724, 726, 811, 869, 894, 895, 902, 912, 942, 961]))
