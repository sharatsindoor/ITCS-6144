def sorting_insertion(arr):
    for ax in range(1, len(arr)): 
        bz = ax-1
        num = arr[ax]
        while bz>=0 and arr[bz]>num:
            arr[bz+1] = arr[bz]
            bz = bz-1
        
    arr[bz+1]=num