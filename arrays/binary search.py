# Binary Search using Recursion

def binary_search(arr, low, high, target):
    if low > high:
        return -1  # Base case: target not found
    mid = (low + high) // 2  # Find the middle index
    if arr[mid] == target:
        return mid  # Target found at mid index
    if arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)  # Search in the right half
    else:
        return binary_search(arr, low, mid - 1, target)  # Search in the left half
    


# ------- Input -------
arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))
arr.sort()   # <-- sorting happens here, before search

target = int(input("Enter number to search: "))

# ------- Call -------
result = binary_search(arr, 0, len(arr) - 1, target)

# ------- Output -------
if result != -1:
    print(f"Element found at index {1+result}")
else:
    print("Element not found")