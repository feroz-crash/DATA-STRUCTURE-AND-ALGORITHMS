def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
# Example usage
def main(): 
    n=int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter numbers: ").split()))[:n]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()