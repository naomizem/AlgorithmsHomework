from itertools import pairwise

# פונקציה לבדיקה אם רשימה ממוינת
def is_sorted(a, key=lambda x: x):
    """
    בודקת אם הרשימה a מסודרת בסדר עולה לפי key.
    מחזירה True אם כן, False אם לא.

    a: רשימה
    key: פונקציה שמחזירה את הערך להשוואה מכל פריט
    """
    for prev, curr in pairwise(a):
        if key(prev) > key(curr):
            return False
    return True


# פונקציה למיזוג שני מערכים ממוינים

def merge(a, b, key=lambda x: x):
    """
    ממזגת שני מערכים מסודרים לפי key.
    אם אחד המערכים אינו ממויין, מחזירה None.

    a, b: רשימות מסודרות
    key: פונקציה שמחזירה את המפתח של כל פריט
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

    # הוספת השארית
    result.extend(a[i:])
    result.extend(b[j:])
    return result


# ==========================
# דוגמאות שימוש
# ==========================
# מיזוג רשימות מספרים
a = [1, 3, 5]
b = [2, 4, 6]
c = [3, 2, 1]  # לא ממויין

print("מיזוג a+b:", merge(a, b))  # [1, 2, 3, 4, 5, 6]
print("מיזוג a+c:", merge(a, c))  # None

# מיזוג רשימות של tuples לפי רכיב ראשון
tuples_a = [(1, 'a'), (3, 'c')]
tuples_b = [(2, 'b'), (4, 'd')]
merged_tuples = merge(tuples_a, tuples_b, key=lambda x: x[0])
print("מיזוג tuples_a + tuples_b:", merged_tuples)
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
