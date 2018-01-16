array = [4, 8, 13, 6, 8, 0, 1, 4.5, 6]
def selection_sort(array):
    a = array
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        min_elem = a[min_idx]
        a[min_idx] = a[i]
        a[i] = min_elem
    return a

print(selection_sort(array))
