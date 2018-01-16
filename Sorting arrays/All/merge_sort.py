def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    res += A[i:] + B[j:]
    return res


def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A)//2]
        R = A[len(A)//2:]
    return merge(merge_sort(L), merge_sort(R))

array = [0, 4, 6, 1, 3, 6, 3]
array = merge_sort(array)
print(array)
