def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(arr, i, heap_size, key=lambda x: x):
    while True:
        l = left(i)
        r = right(i)
        largest = i

        # בדיקה מול הבן השמאלי
        if l < heap_size and key(arr[l]) > key(arr[largest]):
            largest = l

        # בדיקה מול הבן הימני
        if r < heap_size and key(arr[r]) > key(arr[largest]):
            largest = r

        # אם i הוא כבר הגדול ביותר - אין מה לסדר
        if largest == i:
            break

        # החלפה
        arr[i], arr[largest] = arr[largest], arr[i]

        # ממשיכים כלפי מטה
        i = largest
