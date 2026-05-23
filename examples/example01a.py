from sm_core import count_occurrences, predecessor

def main():
    arr1: list[int] = [1, 0, 5, 4, 4]

    print(predecessor(arr1, 0))
    print(count_occurrences(sorted(arr1), 1))

if __name__ == "__main__":
    main()