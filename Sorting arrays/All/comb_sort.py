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


array = [0, 3, 5, 1, 6, 0 ,2]
print(comb_sort(array))
