import sys

# Merge Sort

array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])
    
    merged_arr = []
    i=h=0
    while i < len(low_arr) and h < len(high_arr):
        if low_arr[i] < high_arr[h]:
            merged_arr.append(low_arr[i])
            i+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[i:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr

print('before: ', array)
array = merge_sort(array)
print('after: ', array)
        
