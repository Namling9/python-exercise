# Bubble sort
'''
def bubble_sort(l):
    
    n = len(l)
    for i in range(n):
        swapped = False
        
        for j in range(n-i-1):
            
            if l[j] > l[j+1]:
                
                l[j], l[j+1]=l[j+1], l[j]
                swapped = True
            
        if not swapped:
            break
    
    return l

l = [98,12,31,12,13,42,1,2,3,4,6342,231,12,23,35,10]
print(bubble_sort(l))   #[1, 2, 3, 4, 10, 12, 12, 12, 13, 23, 31, 35, 42, 98, 231, 6342] '''

# Merge Sort
'''
def merge_sort(l):
    
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    
    l_left = l[:mid]
    l_right = l[mid:]
    
    l_left = merge_sort(l_left)
    l_right = merge_sort(l_right)
    
    return merge(l_left,l_right)

def merge(l_left,l_right):
    
    result = []
    i,j = 0,0
    
    while i < len(l_left) and j < len(l_right):
        
        if l_left[i] < l_right[j]:
            
            result.append(l_left[i])
            i+=1
            
        else: 
            result.append(l_right[j])
            j+=1
            
    result.extend(l_left[i:])
    result.extend(l_right[j:])

    return result

l = [98,12,31,12,13,42,1,2,3,4,6342,231,12,23,35,10]
print(merge_sort(l))   #[1, 2, 3, 4, 10, 12, 12, 12, 13, 23, 31, 35, 42, 98, 231, 6342] 
'''
        
# Quick sort

def quick_sort(l,low,high):
    
    if low < high:
        
        pivot = partition(l,low,high)
        quick_sort(l,low,pivot-1)
        quick_sort(l,pivot+1,high)
    
    return l

def partition(l,low,high):
    
    p = l[low]
    i = low + 1
    j = high
    
    while True:
        
        while i <= j and l[i] <= p:
            i+=1
        
        while i <= j and l[j] >= p:
            j-=1
        
        if i < j:
            
            l[i],l[j]=l[j],l[i]
        
        else: break
    
    l[low], l[j]=l[j], l[low]
    
    return j

l = [98,12,31,12,13,42,1,2,3,4,6342,231,12,23,35,10]
print(quick_sort(l,0,len(l)-1))   #[1, 2, 3, 4, 10, 12, 12, 12, 13, 23, 31, 35, 42, 98, 231, 6342] 
print(l)

       
            