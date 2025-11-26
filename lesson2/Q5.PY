def dual_pivot_partition(a, key=lambda x: x):
    """
    מחלק את הרשימה לשלושה חלקים לפי שני pivots.

    a: רשימה לא מסודרת
    key: פונקציה שמחזירה את המפתח לכל פריט

    מחזירה את האינדקסים של שני הפיבוטים לאחר החלוקה: (lp, rp)
    """
    if len(a) < 2:
        return 0, len(a) - 1  # אם יש פחות מ-2 פריטים

    # בוחרים שני pivots: הראשון והאחרון
    if key(a[0]) > key(a[-1]):
        a[0], a[-1] = a[-1], a[0]  # מבטיחים pivot1 <= pivot2

    pivot1 = a[0]
    pivot2 = a[-1]
    pivot1_key = key(pivot1)
    pivot2_key = key(pivot2)

    i = 1  # סמן לפריטים קטנים מ-pivot1
    j = 1  # סמן לעבור על הרשימה
    k = len(a) - 1  # סמן לפריטים גדולים מ-pivot2

    while j <= k:
        if key(a[j]) < pivot1_key:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif key(a[j]) > pivot2_key:
            a[j], a[k] = a[k], a[j]
            k -= 1
        else:
            j += 1

    # העברת הפיבוטים למקומם הסופי
    a[0], a[i - 1] = a[i - 1], a[0]  # pivot1
    a[-1], a[k + 1] = a[k + 1], a[-1]  # pivot2

    return i - 1, k + 1  # אינדקסים סופיים של שני הפיבוטים


# דוגמה לשימוש
lst = [9, 3, 7, 1, 5, 8, 2, 6, 4]
lp, rp = dual_pivot_partition(lst)
print("רשימה לאחר dual-pivot partition:", lst)
print("מיקום pivot1:", lp, "מיקום pivot2:", rp)
