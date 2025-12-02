def parent(i):
    return (i - 1) // 2

def is_max_heap(arr, i=0, key=lambda x: x):
    if len(arr) <= 1:
        return True

    for j in range(i + 1, len(arr)):
        p = parent(j)
        if key(arr[p]) < key(arr[j]):
            return False

    return True
