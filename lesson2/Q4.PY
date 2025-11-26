
# פונקציית partition בשיטת Lomuto
def partition_lomuto(a, key=lambda x: x):
    """
    מימוש של partition בשיטת Lomuto.

    a: רשימה לא מסודרת
    key: פונקציה שמחזירה את המפתח מכל פריט

    מחזירה את האינדקס של ה-pivot לאחר המיון.
    """
    pivot = a[-1]  # נבחר הפריט האחרון בתור pivot
    pivot_key = key(pivot)
    i = -1  # הסמן של האלמנטים הקטנים מ-pivot

    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_key:
            i += 1
            a[i], a[j] = a[j], a[i]  # החלפה
    # העברת ה-pivot למקומו הסופי
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1


# פונקציית partition בשיטת Hoare
def partition_hoare(a, key=lambda x: x):
    """
    מימוש של partition בשיטת Hoare.

    a: רשימה לא מסודרת
    key: פונקציה שמחזירה את המפתח מכל פריט

    מחזירה אינדקס של pivot (או מיקום של הפריט הראשון שגדול ממנו)
    """
    pivot = a[0]  # בוחרים את האלמנט הראשון בתור pivot
    pivot_key = key(pivot)
    i = -1
    j = len(a)

    while True:
        # מתקדם מימין לשמאל עד שנמצא ערך >= pivot
        i += 1
        while key(a[i]) < pivot_key:
            i += 1

        # מתקדם משמאל לימין עד שנמצא ערך <= pivot
        j -= 1
        while key(a[j]) > pivot_key:
            j -= 1

        if i >= j:
            return j  # החזרת המיקום של הפריט שנמצא במקום נכון

        # החלפה
        a[i], a[j] = a[j], a[i]

# ==========================
# דוגמאות שימוש
# ==========================
# עם מספרים
lst = [9, 3, 7, 1, 5]
pivot_index = partition_lomuto(lst)
print("Lomuto - רשימה לאחר partition:", lst)
print("Lomuto - מיקום pivot:", pivot_index)

lst2 = [9, 3, 7, 1, 5]
pivot_index2 = partition_hoare(lst2)
print("Hoare - רשימה לאחר partition:", lst2)
print("Hoare - מיקום pivot:", pivot_index2)

# עם tuples לפי רכיב ראשון
tuples_list = [(5, 'a'), (2, 'b'), (8, 'c'), (1, 'd')]
pivot_index = partition_lomuto(tuples_list, key=lambda x: x[0])
print("Lomuto - tuples לאחר partition:", tuples_list)
print("Lomuto - מיקום pivot:", pivot_index)

tuples_list2 = [(5, 'a'), (2, 'b'), (8, 'c'), (1, 'd')]
pivot_index2 = partition_hoare(tuples_list2, key=lambda x: x[0])
print("Hoare - tuples לאחר partition:", tuples_list2)
print("Hoare - מיקום pivot:", pivot_index2)
