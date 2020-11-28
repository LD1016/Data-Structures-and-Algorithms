"""

"""


def game(S, A):
    res = [S[0]]
    i = 0
    while len(res) <= len(A):
        i = A[i]
        if i == 0:
            break
        res.append(S[i])
    res = "".join(res)
    return res


print(game('cdeo', [3, 2, 0, 1]))
