def min_max_problem(arr,low,high):
    if low == high:
        min_val = arr[low]
        max_val = arr[low]
        return min_val, max_val
    if high == low + 1:
        if arr[low] < arr[high]:
            min_val = arr[low]
            max_val = arr[high]
        else:
            min_val = arr[high]
            max_val = arr[low]
        return min_val, max_val
    mid = (low + high) // 2
    min1, max1 = min_max_problem(arr, low, mid)
    min2, max2 = min_max_problem(arr, mid + 1, high)
    min_val = min(min1, min2)
    max_val = max(max1, max2)
    return min_val, max_val

# Example usage:
arr = [3, 5, 1, 8, 2, 7]
low = 0
high = len(arr) - 1
min_value, max_value = min_max_problem(arr, low, high)
print("Minimum value:", min_value)
print("Maximum value:", max_value)