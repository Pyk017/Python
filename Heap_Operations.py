h_size = 0


def max_heapify(ar, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and ar[left] > ar[i]:
        largest = left

    if right < heap_size and ar[right] > ar[largest]:
        largest = right

    if largest != i:
        ar[i], ar[largest] = ar[largest], ar[i]
        max_heapify(ar, largest, heap_size)


def min_heapify(ar, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and ar[left] < ar[i]:
        largest = left

    if right < heap_size and ar[right] < ar[largest]:
        largest = right

    if largest != i:
        ar[i], ar[largest] = ar[largest], ar[i]
        min_heapify(ar, largest, heap_size)


def build_max_heap(ar):
    heap_size = len(ar)
    for i in range(len(ar)//2-1, -1, -1):
        max_heapify(ar, i, heap_size)
    return heap_size


def build_min_heap(ar):
    heap_size = len(ar)
    for i in range(len(ar)//2-1, -1, -1):
        min_heapify(ar, i, heap_size)
    return heap_size


def heap_extract_max(ar, heap_size):
    if heap_size < 0:
        print("Heap UnderFlow!")
    maxi = ar[0]
    ar[0] = ar[heap_size-1]
    heap_size -= 1
    max_heapify(ar, 0, heap_size)
    return maxi


def heap_extract_min(ar, heap_size):
    if heap_size < 0:
        print("Heap UnderFlow!")
    mini = ar[0]
    ar[0] = ar[heap_size-1]
    heap_size -= 1
    min_heapify(ar, 0, heap_size)
    return mini


array = list(map(int, input("Enter elements in the Array :- ").split()))
build_max_heap(array)
print("Max-Heap of Your Given Array is :- ", array)
print("Original Array is :- ", array)
print('Maximum in the Heap is :- ', heap_extract_max(array, h_size))
h_size = build_min_heap(array)
print("Min-Heap of Your Given Array is :- ", array)
print('Minimum in the Heap is :- ', heap_extract_min(array, h_size))
