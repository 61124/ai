def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print(*arr)

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input(f"Enter {n} elements separated by spaces: ").split()))
    print("Original array:", end=" ")
    print_array(arr)
    selection_sort(arr)
    print("Array after Selection Sort:", end=" ")
    print_array(arr)

if __name__ == "__main__":
    main()