class Solution: 
    def solve(self, A):
        negArr = []
        posArr = []
        for i in A:
            if i < 0:
                negArr.append(i)
            else:
                posArr.append(i)
        negArr = [x*x for x in negArr]
        posArr = [x*x for x in posArr]
        # print(negArr, posArr)
        return self.merge(self.mergeSort(negArr), self.mergeSort(posArr))

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