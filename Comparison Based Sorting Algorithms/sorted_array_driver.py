import random
import time
import sys
#import matplotlib.pyplot as plot
from statistics import mean
from statistics import mean
from heap_sort import sorting_heap
from insertion_sort import sorting_insertion
from merge_sort import merge_sort
from quick_sort import sorting_quick,mquick_sort

if __name__ == '__main__':
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
    #finding the running-time for the each of the sorting algorithm
    for index in range(0, len(arr)):
        runs = 1
        time_insertion_sorting = []
        time_merge_sorting = []
        time_inplaceQuick_sorting = []
        time_medianQuick_sorting = []
        time_heap_sorting = []
        
        sortedArray = []
        for a in range(0,arr[index]):
            sortedArray.append(a)
        #calculating time for Insertion Sort
        then_time = time.time()
        sorting_insertion(sortedArray[:])
        now_time = time.time()
        time_insertion_sorting.append((now_time-then_time)*1000)
        #calculating time for Merge Sort
        then_time = time.time()
        merge_sort(sortedArray[:])
        now_time = time.time()
        time_merge_sorting.append((now_time-then_time)*1000)
        #calculating time for Heap Sort
        then_time = time.time()
        sorting_heap(sortedArray[:])
        now_time = time.time()
        time_heap_sorting.append((now_time-then_time)*1000)    
        #calculating time for In-Place Quick Sort
        then_time = time.time()
        sorting_quick(sortedArray[:])
        now_time = time.time()
        time_inplaceQuick_sorting.append((now_time-then_time)*1000)
        #calculating time for Modified QuickSort
        then_time = time.time()
        mquick_sort(sortedArray[:])
        now_time = time.time()
        time_medianQuick_sorting.append((now_time-then_time)*1000)            
        #Finding the average value for each of the algorithm
        insertion_sorting_average.append(mean(time_insertion_sorting))
        merge_sorting_average.append(mean(time_merge_sorting))
        heap_sorting_average.append(mean(time_heap_sorting))
        inplaceQuick_sorting_average.append(mean(time_inplaceQuick_sorting))
        medianQuick_sorting_average.append(mean(time_medianQuick_sorting))
        
        
    print("ARRAY INPUT SIZES RANGES:\n",arr)
    print("INSERTION SORT TIME FOR VARIOUS INPUT SIZES:\n",insertion_sorting_average)
    print("MERGE SORT TIME FOR VARIOUS INPUT SIZES:\n",merge_sorting_average)
    print("HEAP SORT TIME FOR VARIOUS INPUT SIZES:\n",heap_sorting_average)
    print("IN-PLACE QUICK SORT TIME FOR VARIOUS INPUT SIZES:\n",inplaceQuick_sorting_average)
    print("MODIFIED QUICK SORT TIME FOR VARIOUS INPUT SIZES:\n",medianQuick_sorting_average)
