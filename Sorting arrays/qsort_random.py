import random


def qsort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)

        l_array = [n for n in array if n < q]
        e_array = [q] * array.count(q)
        b_array = [n for n in array if n > q]
        return qsort(l_array) + e_array + qsort(b_array)


array = [5, 0, 1, 3, 8, 9]
print(qsort(array))
