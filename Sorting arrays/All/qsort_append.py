import random


def qsort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        s_array = []
        m_array = []
        e_array = []
        for n in array:
            if n < q:
                s_array.append(n)
            elif n > q:
                m_array.append(n)
            else:
                e_array.append(n)
        return qsort(s_array) + e_array + qsort(m_array)


array = [5, 0, 1, 3, 8, 9]
print(qsort(array))
