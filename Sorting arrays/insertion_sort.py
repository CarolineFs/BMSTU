array = [4,5,8,1,0,5]

def insetrion_sort(array):
    a = array
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j -= 1
        a[j] = v
    return a

print(insetrion_sort(array))
