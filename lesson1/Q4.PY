from random_tuples import create_random_tuples


# סעיף א

def min_find(a, key):
    if not a:
        raise ValueError("List is empty")

    min_val = a[0]
    max_val = a[0]

    for item in a[1:]:
        if key(item) < key(min_val):
            min_val = item
        if key(item) > key(max_val):
            max_val = item

    return min_val, max_val


# סעיף ב
def run_Q4():
    arr = create_random_tuples(100, 3, [int, float, str])

    min_item, max_item = min_find(arr, key=lambda x: x[2])

    print("min=", min_item)
    print("max=", max_item)


