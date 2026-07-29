n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements separated by space: ").split()))

def min_max(arr, low, high):
    # Base case: only one element
    if low==high:
        return arr[low], arr[high]
    if low==high-1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        elif arr[low] > arr[high]:
            return arr[high], arr[low]
    else:
        mid=high-(high-low)//2
        min1, max1 = min_max(arr, low, mid)
        min2,max2=min_max(arr, mid+1, high)
        if min1<min2:
            return min1, max(max1,max2)
        else:
            return min2, max(max1,max2)

result_min, result_max = min_max(arr, 0, n - 1)
print("Minimum:", result_min)
print("Maximum:", result_max)