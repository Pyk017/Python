def heapify(ar, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < heap_size and ar[left] < ar[i]:
        smallest = left
    if right < heap_size and ar[right] < ar[smallest]:
        smallest = right
    if smallest != i:
        ar[i], ar[smallest] = ar[smallest], ar[i]
        heapify(ar, smallest, heap_size)


def build_min_heap(ar):
    heap_size = len(ar)
    for i in range(len(ar)//2-1, -1, -1):
        heapify(ar, i, heap_size)

    return heap_size
# 1 3 10 25 30 20 100


def heap_extract_min(ar, heap_size):
    if heap_size < 0:
        print("Heap Underflow!")
    mini = ar[0]
    ar[0] = ar[heap_size-1]
    heap_size -= 1
    heapify(ar, 0, heap_size)
    return mini


def heap_decrease_key(ar, i, key):
    if key > ar[i] and i < len(ar):
        print("Heap Underflow!")
        return
    ar[i] = key
    while i != 0 and ar[i//2] > ar[i]:
        ar[i], ar[i//2] = ar[i//2], ar[i]
        i //= 2


def heap_increase_key(ar, i, key, heap_size):
    ar[i] = key
    heapify(ar, i, heap_size)


array = list(map(int, input("Enter elements in the Array :- ").split()))
h_size = build_min_heap(array)
print("Min-Heap elements are :- ", array)
print("Minimum in the heap is :- ", heap_extract_min(array, h_size))
print("Min-Heap elements are :- ", array)
target, k = list(map(int, input("Enter position and key to decrease the key :- ").split()))
heap_decrease_key(array, target, k)
print("New heap is :- ", array)
