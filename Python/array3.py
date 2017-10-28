arr = []
arr = input('Введите элементы массива через пробел: ').split()
for i in range(len(arr)):
    arr[i] = float(arr[i])
print()
print(arr)

max_elem = min_elem = arr[0]
max_ind = min_ind = k_pos = k_neg = 0

for i in range (len(arr)):
    if arr[i] > 0: k_pos += 1
    if arr[i] < 0: k_neg += 1
    if arr[i] > max_elem:
        max_elem = arr[i]
        max_ind = i
    if arr[i] < min_elem:
        min_elem = arr[i]
        min_ind = i
r = abs(max_ind - min_ind) - 1

print('\nКоличество положительных элементов массива =', k_pos)
print('\nКоличество отрицательных элементов массива =', k_neg)
print('\nРасстояние между максимальным и минимальным элементом =', r)
    
