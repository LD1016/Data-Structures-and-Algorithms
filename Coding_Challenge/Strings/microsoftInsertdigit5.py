"""
You are given an integer (in finite range [-N, N]) 
and you wish to maximize the number by inserting somewhere the digit '5'.

example: 
'128'   -> '5128'
'0'     -> '50'
'678'   -> '6785'
'748'   -> '7548'
'-999'  -> '-5999'
"""


def solution(A):
    res = []
    stringNum = str(A)
    allGreater = True
    neg = 1
    if A < 0:
        neg = -1
        res = ["-"]
        stringNum = stringNum[1:]
    for i in range(len(stringNum)):
        if int(stringNum[i]) * neg < 5 * neg:
            res.append('5')
            res.append(stringNum[i:])
            allGreater = False
            break
        else:
            res.append(stringNum[i])
    if allGreater:
        res.append('5')
    return int("".join(res))


print(solution(128))
print(solution(0))
print(solution(678))
print(solution(748))
print(solution(-999))
print(solution(-74))
print(solution(-47))
