def partition(arr,l,h):
    k=arr[l]
    i=l
    j=h
    while True:
        while True:
            i+=1
            if i>h or arr[i]>k:
                break
        while True:
            j-=1
            if arr[j]<=k:
                break
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[l],arr[j]=arr[j],arr[l]
    return j
def quick_sort(arr,l,h):
    if l<h:
        j=partition(arr,l,h+1)
        quick_sort(arr,l,j-1)
        quick_sort(arr,j+1,h)
if __name__=="__main__":
    arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    arr.append(float('inf'))  # Append infinity to handle the partitioning correctly
    quick_sort(arr, 0, len(arr) - 2)
    print("Sorted array:", arr[:-1])  # Exclude the last element (infinity) from the output

