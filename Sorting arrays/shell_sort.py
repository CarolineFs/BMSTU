def shell_sort(array):
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


array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(array)
print(array)
