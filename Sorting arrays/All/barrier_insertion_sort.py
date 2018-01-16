def barrier_insertion(a):
    for i in range(2, len(a)):
        if a[i-1] > a[i]:
            a[0] = a[i]
            j = i - 1
            while a[j] > a[0]:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = a[0]
    return a


array = [0, 5, 0, 2, 9, 3, 8, 4]
array = barrier_insertion(array)
array = array[1:]
print(array)
