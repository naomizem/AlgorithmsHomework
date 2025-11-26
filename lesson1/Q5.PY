# Q5.py
def sort_insertion(a, key):
    n = len(a)
    for i in range(1, n):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a
