def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def max_heapify(arr, i, heap_size, key=lambda x: x):
    while True:
        l = left(i)
        r = right(i)
        largest = i

        if l < heap_size and key(arr[l]) > key(arr[largest]):
            largest = l

        if r < heap_size and key(arr[r]) > key(arr[largest]):
            largest = r

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr, key=lambda x: x):
    heap_size = len(arr)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, i, heap_size, key)
    return arr


def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr, key)

    heap_size = len(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heap_size -= 1

        max_heapify(arr, 0, heap_size, key)

    return arr
