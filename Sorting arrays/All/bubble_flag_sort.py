def bubble_flag_sort(A):
    j = len(A) - 1
    IsNotOrdered = True
    while IsNotOrdered:
        IsNotOrdered = False
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                IsNotOrdered = True
        j -= 1
    return A


array = [3, 0, 1, 4, 5, 7, 5 ,3, 6]
print(bubble_flag_sort(array))
