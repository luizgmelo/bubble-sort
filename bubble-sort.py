def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

reverse = [5, 4, 3, 2, 1]
random = [3, 2, 4, 1, 5]
order = [1, 2, 3, 4, 5]
bubble_sort(reverse)
bubble_sort(random)
bubble_sort(order)
print(reverse)
print(random)
print(order)

