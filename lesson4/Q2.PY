def partition(arr, left, right, key):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if key(arr[j]) <= key(pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_kth(arr, left, right, k, key=lambda x: x):
    if left == right:
        return arr[left]

    p = partition(arr, left, right, key)

    if k == p:
        return arr[p]
    elif k < p:
        return quick_kth(arr, left, p - 1, k, key)
    else:
        return quick_kth(arr, p + 1, right, k, key)
