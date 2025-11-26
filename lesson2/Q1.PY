from random_tuples import create_random_tuples

tuples_list = create_random_tuples(5, 3, [int, float, str])

print("הרשימה המקורית:")
for t in tuples_list:
    print(t)

sorted_by_int = sorted(tuples_list, key=lambda x: x[0])
print("\nמיון לפי הרכיב הראשון (int):")
for t in sorted_by_int:
    print(t)

sorted_by_float = sorted(tuples_list, key=lambda x: x[1])
print("\nמיון לפי הרכיב השני (float):")
for t in sorted_by_float:
    print(t)

sorted_by_str = sorted(tuples_list, key=lambda x: x[2])
print("\nמיון לפי הרכיב השלישי (str):")
for t in sorted_by_str:
    print(t)
