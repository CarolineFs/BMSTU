array = [4, 6, 1, 0, 3, 2]


def shaker_sort(array):
    left = 1
    right = k = len(array) - 1
    while left < right:
        for i in range(right, left - 1, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                k = i
            left = k
        for i in range(left, right + 1):
            if array[i - 1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
                k = i
            right = k
    return array


print(shaker_sort(array))
