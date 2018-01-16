array = [4, 6, 1, 0, 3, 2]


def shaker_sort(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
        right -= 1
        for i in range(right, left, -1):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
        left += 1
    return array


print(shaker_sort(array))
