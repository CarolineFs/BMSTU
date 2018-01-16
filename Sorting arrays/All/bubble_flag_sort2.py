array = [0, 3, 6, 1, 2]


def bubble_sort(array):
    flag = 0
    n = len(array)
    for i in range(n):
        flag = 0
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
        if not flag:
            return array
    return array


print(bubble_sort(array
