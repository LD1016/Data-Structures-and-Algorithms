class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        rotatedTime = self.rotedArr(A)
        result = -1
        if A[rotatedTime] == B:
            return rotatedTime
        prev, next = (rotatedTime - 1 + len(A)
                      ) % len(A), (rotatedTime+1) % len(A)
        if A[next] <= B <= A[-1]:
            find = self.binarySearch(A[rotatedTime+1:], B)
            result = find + next if find != -1 else result
        elif A[0] <= B <= A[prev]:
            find = self.binarySearch(A[:rotatedTime], B)
            result = find if find != -1 else result
        return result

    def binarySearch(self, A, target):
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def rotedArr(self, A):
        start, end, n = 0, len(A) - 1, len(A)
        while start <= end:
            if A[start] <= A[end]:
                return start
            mid = (start + end) // 2
            prev, next = (mid - 1 + n) % n, (mid+1) % n
            if A[prev] > A[mid] and A[next] > A[mid]:
                return mid
            elif A[mid] <= A[end]:
                end = mid - 1
            elif A[start] <= A[mid]:
                start = mid + 1
        return -1


test = Solution()
print(test.search([101, 103, 106, 109, 158, 164, 182, 187,
                   202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100], 202))
print(test.search([180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177],
                  42))
