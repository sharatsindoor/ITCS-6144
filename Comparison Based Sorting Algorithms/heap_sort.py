heap_entered=[]
arr_size=0
arr_sorted=[]

def heap_generate(sequence):
    global heap_entered
    heap_entered = [0] * (len(sequence)+1)
    for ax in range(0,len(sequence)):
        enter(sequence[ax])

def enter(x):
    global arr_size
    arr_size = arr_size +1
    po=arr_size
    heap_entered[po]=x
    up_shift_bubble(po)

def shift(a,b):
    temp_var = heap_entered[a]
    heap_entered[a] = heap_entered[b]
    heap_entered[b] = temp_var

def down_shift(lm):
    small = lm
    LC_ID = 2 * lm
    RC_ID = 2 * lm + 1
    if (LC_ID < arr_size  and heap_entered[small] > heap_entered[LC_ID]):
        small = LC_ID
    if (RC_ID < arr_size  and heap_entered[small] > heap_entered[RC_ID]):
        small = RC_ID
    if (small != lm):
        shift(lm, small)
        down_shift(small)

def sorting_heap1(sequence):
    heap_generate(sequence)

def up_shift_bubble(place):
    x_id = place // 2
    y_id = place
    while (heap_entered[x_id] > heap_entered[y_id] and y_id > 0):
        shift(y_id, x_id)
        y_id = x_id
        x_id = x_id // 2
        
def min_find():
    global arr_size
    small = heap_entered[1]
    heap_entered[1]=heap_entered[arr_size]
    heap_entered[arr_size] = 0
    down_shift(1)
    arr_size=arr_size -1
    return small



def sorting_heap(sequence):
    arr_sorted=[0]*len(sequence)
    sorting_heap1(sequence)
    for ax in range(0,len(sequence)):
        arr_sorted[ax]=min_find()
    return arr_sorted