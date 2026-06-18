def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
            print(arr)
        
        if count == 0:
            print("Array is sorted:")
            break
        count = 0

    return arr
# Example usage
def main():
    n=int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter numbers: ").split()))[:n]
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()