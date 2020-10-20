def insertionSort(arr): 
    # tempArr = [arr[0]]
    # i = 1
    # while i < len(arr):
    #     if arr[i-1] < arr[i]:
    #         tempArr.append(arr[i])
    #     else:    
    #         for j in range(len(tempArr)):
    #             if arr[i] < arr[j]:
    #                 tempArr = tempArr[:j] + [arr[i]] + tempArr[j:]
    #                 i += 1
    #     i += 1
    # return tempArr
    i = 1 
    curr = arr[0]
    while i < len(arr):
        if curr > arr[i]:
            valI = arr.pop(i)
            for j in range(i):
                if arr[j] > valI: 
                    arr.insert(j, valI)
                    break 
        curr = arr[i]
        i += 1
    return arr 


print(insertionSort([1, 5, 9, 2, 3]))