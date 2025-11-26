from itertools import pairwise


# פונקציה לבדיקה אם רשימה ממוינת
def is_sorted(a, key=lambda x: x):
    """
    בודקת אם הרשימה a מסודרת בסדר עולה לפי key.
    מחזירה True אם כן, False אם לא.
    """
    for prev, curr in pairwise(a):
        if key(prev) > key(curr):
            return False
    return True


# פונקציה למיזוג שתי רשימות ממוינות
def merge_two_sorted(a, b, key=lambda x: x):
    """
    ממזגת שתי רשימות ממוינות לפי key.
    מחזירה רשימה ממוינת או None אם אחד מהמערכים לא ממויין.
    """
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


# פונקציה למיזוג כמה רשימות ממוינות
def merge_sorted_lists(lists, key=lambda x: x):
    """
    ממזגת מספר רשימות ממוינות לרשימה אחת ממוינת.

    lists: רשימה של רשימות ממוינות
    key: פונקציה שמחזירה את המפתח של כל פריט
    """
    if not lists:
        return []

    merged = lists[0]

    for lst in lists[1:]:
        merged = merge_two_sorted(merged, lst, key)
        if merged is None:
            return None  # אם אחת מהרשימות לא מסודרת

    return merged


# דוגמה לשימוש

lists_of_numbers = [
    [1, 4, 6],
    [2, 5, 8],
    [0, 3, 7]
]

merged_result = merge_sorted_lists(lists_of_numbers)
print(merged_result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# עם tuples לפי רכיב ראשון
lists_of_tuples = [
    [(1, 'a'), (3, 'c')],
    [(2, 'b'), (4, 'd')],
    [(0, 'x'), (5, 'y')]
]

merged_tuples = merge_sorted_lists(lists_of_tuples, key=lambda x: x[0])
print(merged_tuples)
# [(0, 'x'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'y')]
