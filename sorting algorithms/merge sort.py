def merge_sort(arr, left, right):
    if left==right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    b=[]
    j=mid+1
    h=left
    while h<=mid and j<=right:
        if arr[h]<arr[j]:
            b.append(arr[h])
            h+=1
        else:
            b.append(arr[j])
            j+=1
    # Append any remaining elements from either subarray
    while h<=mid:
        b.append(arr[h])
        h+=1
    while j<=right:
        b.append(arr[j])
        j+=1
    # Copy the merged elements back to the original array
    for i in range(len(b)):
        arr[left + i] = b[i]
arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)