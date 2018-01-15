array = [0, 4, 1, 6, 2, 6]


def binary_insertion_sort(array):
    for i in range(2, len(array)):
        if array[i-1] > array[i]:
            x = array[i]
            left = 1
            right = len(array) - 1
            while True:
                middle = (left + right)//2
                if array[middle] < x:
                    left = middle + 1
                else:
                    right = middle - 1
                if left > right:
                    break
            for j in range(left, i-1, -1):
                array[j+1] = array[j]
            array[left] = x
    return array

print(binary_insertion_sort(array))
