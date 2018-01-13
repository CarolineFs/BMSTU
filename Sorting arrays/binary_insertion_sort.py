def binary_insertion(array):
    for i in range(1, len(array)):
        left = 0
        right = i - 1
        middle = (left + right+1)//2
        print(middle)
        while True:
            print(array[i], array[middle])
            if array[i] > array[middle]:
                left = middle
            else:
                right = middle
            middle = (left + right+1)//2
            print(left, right, middle)
            if middle == i - 1:
                break


array = [1,2,3,5,4]
binary_insertion(array)
