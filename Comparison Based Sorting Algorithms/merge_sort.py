def merge_sort(arr):
    if len(arr)>1:
        m = len(arr)//2
        larr = arr[:m]
        rarr = arr[m:]

        merge_sort(larr)
        merge_sort(rarr)

        ij=0
        kl=0
        mn=0
        while ij < len(larr) and kl < len(rarr):
            if larr[ij] < rarr[kl]:
                arr[mn]=larr[ij]
                ij=ij+1
            else:
                arr[mn]=rarr[kl]
                kl=kl+1
            mn=mn+1

        while ij < len(larr):
            arr[mn]=larr[ij]
            ij=ij+1
            mn=mn+1

        while kl < len(rarr):
            arr[mn]=rarr[kl]
            kl=kl+1
            mn=mn+1
    return (arr)
