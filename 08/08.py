def contains(arr, val):
    if len(arr) == 0:
        return False
    
    mid = len(arr)//2
    return arr[mid] == val or contains(arr[:mid], val) or contains(arr[mid+1:], val)