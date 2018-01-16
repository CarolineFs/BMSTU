def binary_insertion_sort(array):
    for i in range(2, len(array)):
        if array[i-1] > array[i]:
            x = array[i]
            left = 1
            right = i - 1
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


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def bubble_flag_sort(array):
    j = len(array) - 1
    flag = True
    while flag:
        flag = False
        for i in range(0, j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
        j -= 1
    return array


def comb_sort(array):
    alen = len(array)
    gap = (alen*10//13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = 0
        for i in range(alen - gap):
            if array[i+gap] < array[i]:
                array[i], array[i+gap] = array[i+gap], array[i]
                swapped = 1
        gap = (gap * 10 // 13) or swapped
    return array


def barrier_insertion(array):
    for i in range(2, len(array)):
        if array[i-1] > array[i]:
            v = array[i]
            j = i - 1
            while array[j] > v:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = v
    return array


def merge_sort(array):
    def merge(l, r):
        res = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        res += l[i:] + r[j:]
        return res

    def main(array):
        if len(array) <= 1:
            return array
        else:
            left = array[:len(array)//2]
            right = array[len(array)//2:]
        return merge(main(left), main(right))

    array = main(array)

    return array


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


def qsort(L):
    if L: return qsort([x for x in L if x<L[0]]) + [x for x in L if x==L[0]] + \
                 qsort([x for x in L if x>L[0]])
    return []


def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        min_elem = array[min_idx]
        array[min_idx] = array[i]
        array[i] = min_elem
    return array


def shell_sort(array):
    def main(array):
        sublist_count = len(array)//2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                gap_insertion_sort(array,start_position,sublist_count)
            sublist_count //= 2

    def gap_insertion_sort(array, start, gap):
        for i in range(start+gap, len(array), gap):
            current_value = array[i]
            position = i
            while position >= gap and array[position - gap] > current_value:
                array[position]=array[position-gap]
                position -= gap
                array[position] = current_value
    main(array)
    return array
