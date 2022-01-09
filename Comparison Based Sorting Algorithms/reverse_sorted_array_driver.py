import random
import time
import sys
from statistics import mean
from heap_sort import sorting_heap
from insertion_sort import sorting_insertion
from merge_sort import merge_sort

def sortingquick(arr, smallest, highest):
    if smallest < highest:
        op = parting(arr, smallest, highest)
        sortingquick(arr, smallest, op - 1)
        sortingquick(arr, op + 1, highest)

def sorting_quick(numbers):
    arr = numbers
    sortingquick(arr, 0, len(arr) - 1)
    return arr

def parting(arr, smallest, highest):
    ax = (smallest - 1)
    pivot_point = arr[random.randint(smallest,highest)]
    for bz in range(smallest, highest):
        if arr[bz] <= pivot_point:
            ax = ax + 1
            arr[ax], arr[bz] = arr[bz], arr[ax]
    arr[ax + 1], arr[highest] = arr[highest], arr[ax + 1]
    return (ax + 1)
#Selecting the median element
middleC = 0
def middle1(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

def quicksort_middle(arruence, smallest_index, highest_index):
    global middleC
    if smallest_index+ 10  <= highest_index:
        new_pivot_index = partition_median(arruence, smallest_index, highest_index)

        middleC += (highest_index - smallest_index - 1)
        quicksort_middle(arruence, smallest_index, new_pivot_index)
        quicksort_middle(arruence, new_pivot_index + 1, highest_index)

    else:
        insertion_sortting(arruence,smallest_index,highest_index)

def partition_median(arruence, smallest_val_arr, highest_val_arr):
    small_value= arruence[smallest_val_arr]
    high_value = arruence[highest_val_arr - 1]
    length = highest_val_arr - smallest_val_arr
    middle = arruence[smallest_val_arr + length // 2]
    pivot_point = middle1(small_value, high_value, middle)
    pivot_index = arruence.index(pivot_point)
    arruence[pivot_index] = arruence[smallest_val_arr]
    arruence[smallest_val_arr] = pivot_point
    ax = smallest_val_arr + 1
    for bz in range(smallest_val_arr + 1, highest_val_arr):
        if arruence[bz] < pivot_point:
            temp_var = arruence[bz]
            arruence[bz] = arruence[ax]
            arruence[ax] = temp_var
            ax += 1

    high_End_Val = arruence[smallest_val_arr]
    arruence[smallest_val_arr] = arruence[ax - 1]
    arruence[ax - 1] = high_End_Val
    return ax - 1

def mquick_sort(arr):
    quicksort_middle(arr, 0, len(arr))
    return arr

def insertion_sortting(arruence,a,b):
    for ax in range(a, b):
        bz = ax
        while bz > 0 and arruence[bz] < arruence[bz-1]:
            arruence[bz],arruence[bz-1]=arruence[bz-1],arruence[bz]
            bz = bz - 1

if __name__ == '__main__':
    #Setting the recursion Limit
    sys.setrecursionlimit(10**6)#For quick-sort to run properly for large data sets
    arr=[]#INPUT SIZE ARRAY
    for size in range(1000,10001,1000):
        arr.append(size)
    for size in range(20000,60001,10000):
        arr.append(size)
    insertion_sorting_average = [] 
    merge_sorting_average = []
    heap_sorting_average = []
    inplaceQuick_sorting_average = []
    medianQuick_sorting_average = []
    #finding the running time for each of the algorithm
    for index in range(0, len(arr)):
        runs = 1
        time_insertion_sorting = []
        time_merge_sorting = []
        time_inplaceQuick_sorting = []
        time_medianQuick_sorting = []
        time_heap_sorting = []
        #Reversed sorted array
        reversedArray = []
        for a in range(arr[index],0,-1):
            reversedArray.append(a)
        #calculating time for Insertion Sort    
        then_time = time.time()
        sorting_insertion(reversedArray[:])
        now_time = time.time()
        time_insertion_sorting.append((now_time-then_time)*1000)
        #calculating time for Merge Sort
        then_time = time.time()
        merge_sort(reversedArray[:])
        now_time = time.time()
        time_merge_sorting.append((now_time-then_time)*1000)
         #calculating time for Heap Sort
        then_time = time.time()
        sorting_heap(reversedArray[:])
        now_time = time.time()
        time_heap_sorting.append((now_time-then_time)*1000)   
        #calculating time for In-place Quick Sort
        then_time = time.time()
        sorting_quick(reversedArray[:])
        now_time = time.time()
        time_inplaceQuick_sorting.append((now_time-then_time)*1000)
        #calculating time for Modified Quick Sort
        then_time = time.time()
        mquick_sort(reversedArray[:])
        now_time = time.time()
        time_medianQuick_sorting.append((now_time-then_time)*1000)            
        #Finding the mean for each of the running time complexity
        insertion_sorting_average.append(mean(time_insertion_sorting))
        merge_sorting_average.append(mean(time_merge_sorting))
        heap_sorting_average.append(mean(time_heap_sorting))
        inplaceQuick_sorting_average.append(mean(time_inplaceQuick_sorting))
        medianQuick_sorting_average.append(mean(time_medianQuick_sorting))
        
   #Printing Running time value for each of the input size
    print("ARRAY INPUT SIZES RANGES:\n",arr)
    print("INSERTION SORT TIME FOR VARIOUS INPUT SIZES:\n",insertion_sorting_average)
    print("MERGE SORT TIME FOR VARIOUS INPUT SIZES:\n",merge_sorting_average)
    print("HEAP SORT TIME FOR VARIOUS INPUT SIZES:\n",heap_sorting_average)
    print("IN-PLACE QUICK SORT TIME FOR VARIOUS INPUT SIZES:\n",inplaceQuick_sorting_average)
    print("MODIFIED QUICK SORT TIME FOR VARIOUS INPUT SIZES:\n",medianQuick_sorting_average)

    