from Q4 import run_Q4
from Q5 import sort_insertion
from random_tuples import create_random_tuples

def main():
    print("===  Q4 ===")
    run_Q4()

    print("\n===  Q5 ===")

    lists = [
        create_random_tuples(10, 3, [int, float, str]),
        create_random_tuples(10, 3, [int, float, str]),
        create_random_tuples(10, 3, [int, float, str])
    ]

    keys = [lambda x: x[0], lambda x: x[1], lambda x: x[2]]

    for i, lst in enumerate(lists):
        print(f"\nרשימה {i + 1} לפני מיון:")
        for t in lst:
            print(t)

        sort_insertion(lst, key=keys[i])

        print(f"\nרשימה {i + 1} אחרי מיון לפי הפריט {i}:")
        for t in lst:
            print(t)

if __name__ == "__main__":
    main()
