def selectionSort(A):
    # Traverse through all array elements 
    for i in range(len(A)): 
      
        # Find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx].numberUnavailable > A[j].numberUnavailable: 
                min_idx = j 
              
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
        
    return

def combineSchedules(schedule1, schedule2):
    combinedSchedule = []
    for pair in zip(schedule1, schedule2):
        combinedSchedule.append(pair[0] + pair[1])
    return combinedSchedule

def FindDifference(list1, list2):
    return(list(set(list1) - set(list2)))
