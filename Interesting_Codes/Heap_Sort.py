<<<<<<< HEAD
def heapify(ar, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and ar[left] > ar[i]:
        largest = left
    if right < heap_size and ar[right] > ar[largest]:
        largest = right
    if largest != i:
        ar[i], ar[largest] = ar[largest], ar[i]
        heapify(ar, largest, heap_size)


def build_heap(ar):
    heap_size = len(ar)
    for i in range(len(ar)//2-1, -1, -1):
        heapify(ar, i, heap_size)

    return heap_size


def heap_sort(ar):
    heap_size = build_heap(ar)
    for i in range(len(ar)-1, 0, -1):
        ar[0], ar[i] = ar[i], ar[0]
        heap_size -= 1
        heapify(ar, 0, heap_size)

    return ar


array = list(map(int, input("Enter elements in the Array :- ").split()))
print("Sorted Elements in the Array using Heap Sort is :- ", ' '.join(list(map(str, heap_sort(array)))))
=======
def heapify(ar, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and ar[left] > ar[i]:
        largest = left
    if right < heap_size and ar[right] > ar[largest]:
        largest = right
    if largest != i:
        ar[i], ar[largest] = ar[largest], ar[i]
        heapify(ar, largest, heap_size)


def build_heap(ar):
    heap_size = len(ar)
    for i in range(len(ar)//2-1, -1, -1):
        heapify(ar, i, heap_size)

    return heap_size


def heap_sort(ar):
    heap_size = build_heap(ar)
    for i in range(len(ar)-1, 0, -1):
        ar[0], ar[i] = ar[i], ar[0]
        heap_size -= 1
        heapify(ar, 0, heap_size)

    return ar


array = list(map(int, input("Enter elements in the Array :- ").split()))
print("Sorted Elements in the Array using Heap Sort is :- ", ' '.join(list(map(str, heap_sort(array)))))
>>>>>>> Python repo committed
