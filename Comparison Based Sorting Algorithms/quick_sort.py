import random
#Paritioning the array
def parting(seq, smallest, highest):
    ax = (smallest - 1)
    pivot_point = seq[random.randint(smallest,highest)]
    for bz in range(smallest, highest):
        if seq[bz] <= pivot_point:
            ax = ax + 1
            seq[ax], seq[bz] = seq[bz], seq[ax]
    seq[ax + 1], seq[highest] = seq[highest], seq[ax + 1]
    return (ax + 1)
# Sorting based on the smalledt and highest element
def sortingquick(seq, smallest, highest):
    if smallest < highest:
        op = parting(seq, smallest, highest)
        sortingquick(seq, smallest, op - 1)
        sortingquick(seq, op + 1, highest)

def sorting_quick(numbers):
    seq = numbers
    sortingquick(seq, 0, len(seq) - 1)
    return seq

#Selecting the median element
middleC = 0
def middle1(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

def partition_median(sequence, smallest_val_seq, highest_val_seq):
    length = highest_val_seq - smallest_val_seq
    middle = sequence[smallest_val_seq + length // 2]
    small_value = sequence[smallest_val_seq]
    high_value = sequence[highest_val_seq - 1]
    pivot_point = middle1(small_value, high_value, middle)
    pivot_index = sequence.index(pivot_point)
    sequence[pivot_index] = sequence[smallest_val_seq]
    sequence[smallest_val_seq] = pivot_point
    ax = smallest_val_seq + 1
    for bz in range(smallest_val_seq + 1, highest_val_seq):
        if sequence[bz] < pivot_point:
            temp_var = sequence[bz]
            sequence[bz] = sequence[ax]
            sequence[ax] = temp_var
            ax += 1
    high_End_Val = sequence[smallest_val_seq]
    sequence[smallest_val_seq] = sequence[ax - 1]
    sequence[ax - 1] = high_End_Val
    return ax - 1
#implementing the quicksort-Median
def quicksort_middle(sequence, smallest_index, highest_index):
    global middleC
    if smallest_index+ 10  <= highest_index:
        new_pivot_index = partition_median(sequence, smallest_index, highest_index)

        middleC += (highest_index - smallest_index - 1)
        quicksort_middle(sequence, smallest_index, new_pivot_index)
        quicksort_middle(sequence, new_pivot_index + 1, highest_index)

    else:
        insertion_sortting(sequence,smallest_index,highest_index)

def mquick_sort(seq):
    quicksort_middle(seq, 0, len(seq))
    return seq
#Performing the insertion sort when the array size becomes less than 10
def insertion_sortting(sequence,a,b):
    for ax in range(a, b):
        bz = ax
        while bz > 0 and sequence[bz] < sequence[bz-1]:
            sequence[bz],sequence[bz-1]=sequence[bz-1],sequence[bz]
            bz = bz - 1


