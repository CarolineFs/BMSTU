import random

def print_matrix(matrix, size):
    for i in range(size):
        print(matrix[i])


def create_matrix(size, max_sum):
    s = (-1, 1)
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            dec = random.randint(1, max_sum)
            ed = random.randint(0, max_sum - dec)
            new_num = dec*10 + ed
            sign = random.choice(s)
            new_num *= sign
            matrix[i].append(new_num)
    print('Matrix has been generated!')
    print_matrix(matrix, size)
    return matrix


def count_negative(matrix, size):
    k = 0
    for i in range(size):
        for j in range(size):
            if j > i and matrix[i][j] < 0:
                k += 1
    return k


def count_positive(matrix, size):
    k = 0
    for i in range(size):
        for j in range(size):
            if j < i and matrix[i][j] > 0:
                k += 1
    return k


def get_size():
    size = input('Input size: ')

    while not size.isdigit():
        print('Incorrect size!')
        size = input('Input size: ')
    size = int(size)
    return size


def get_max_sum():
    max_sum = input('Input max sum: ')
    try:
        max_sum = int(max_sum)
    except ValueError:
        print('Incorrect input!')
    if type(max_sum) is int:
        if max_sum > 0 and max_sum <= 18:
            return max_sum
        else:
            print('Incorrect input!')
            return ''
        
    
def show_info(k_neg, k_pos):
    print('Negative elements upper main diagonal: ', k_neg)
    print('Positive elements lover main diagonal: ', k_pos)


def main():
    size = get_size()
    max_sum = ''
    while type(max_sum) is not int:
        max_sum = get_max_sum()

    print('Generating matrix...')
    matrix = create_matrix(size, max_sum)

    k_neg = count_negative(matrix, size)
    k_pos = count_positive(matrix, size)

    show_info(k_neg, k_pos)
   
   
main()
