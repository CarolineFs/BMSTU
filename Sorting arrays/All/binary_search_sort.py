import random

# CONST
FLOOR_FOR_ARRAYS = -50
CEIL_FOR_ARRAYS = 50
STEP_FOR_ARRAYS = 1


def create_random_array(size):
    array = []
    for i in range(size):
        array.append(random.randrange(FLOOR_FOR_ARRAYS, CEIL_FOR_ARRAYS,
                                      STEP_FOR_ARRAYS))
    return array


def sort_bin_insert(array):
    n = len(array)
    for i in range(1, n):
        if array[i-1] > array[i]:
            x = array[i]
            left = 0
            right = i - 1
            while True:
                sred = (left + right)//2
                if array[sred] < x:
                    left = sred + 1
                else:
                    right = sred -1
                if left > right:
                    break
            j = i - 1
            while j >= left:
                array[j+1] = array[j]
                j -= 1
            array[left] = x
    return array


random_array_len = 10
random_array = create_random_array(random_array_len)
print('Исходный массив: ')
print(random_array)
print()
random_array = sort_bin_insert(random_array)
print('Отсортированный массив: ')
print(random_array)
