import numpy as np
import pandas as pd
import seaborn as sns
import csv
import time
import tracemalloc
from scipy import stats
import SortingFunctions as sort
import Helpers as helpers
import datetime as dt

def sortednessMeasure(array, sortedArray, measurementType, sortType, Outputfile): 
    increment = .01
    prevSorteness = -1
    t = []
    df = pd.DataFrame()
    for i in range(1, len(array)):   
                rho, pvalue = stats.spearmanr(array, sortedArray)
                sortedness = round(rho, 2)
                if (sortedness >= prevSorteness+increment):                  
                    if measurementType == 1:
                        t = TakeTimeMeasurement(array, t, sortType)
                    if measurementType == 2:
                        t = TakeMemoryMeasurement(array, t, sortType)
                    df[sortedness] = t
                    if (sortedness == 1):
                        break
                    prevSorteness = sortedness
                item = array[i]
                j = i-1
                while j >= 0 and item < array[j]: 
                        array[j+1] = array[j] 
                        j -= 1
                array[j+1] = item 

    df.to_csv(index=False, sep=",", path_or_buf=Outputfile) 

        

def TakeTimeMeasurement(array, t, sortType):
    t = []   
    for y in range(5):
       arrayMeasure = array.copy()
       startTime = time.time()
       if sortType == 1:
        sort.selectionSort(arrayMeasure)
       if sortType == 2:
        sort.insertionSort(arrayMeasure)
       if sortType == 3:
         sort.bubbleSort(arrayMeasure)
       if sortType == 4:
         sort.mergeSort(arrayMeasure)
       if sortType == 5:
         sort.quickSort(arrayMeasure, 0, len(arrayMeasure)-1)
       endTime = time.time()
       t.append(endTime - startTime)
    return t


def TakeMemoryMeasurement(array, t, sortType):
    t = []
    for y in range(5):
       arrayMeasure = array.copy()
       tracemalloc.start()
       if sortType == 1:
        sort.selectionSort(arrayMeasure)
       if sortType == 2:
        sort.insertionSort(arrayMeasure)
       if sortType == 3:
         sort.bubbleSort(arrayMeasure)
       if sortType == 4:
         sort.mergeSort(arrayMeasure)
       if sortType == 5:
         sort.quickSort(arrayMeasure, 0, len(arrayMeasure)-1)
       cur, peak = tracemalloc.get_traced_memory()
       t.append(peak)
       tracemalloc.stop()
    return t



array = helpers.getArray(10, "LoanAmountDataset.csv")
array = sort.quickSort(array, 0, len(array)-1)
reverseSorted = array.copy();
reverseSorted.reverse();

sortednessMeasure(reverseSorted, array, 1,1, "SelectionSortTimeSortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 1,2, "InsertionSortTimeSortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 1,3, "BubbleSortTimeSortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 1,4, "MergeSortTimeSortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 1,5, "QuickSortTimeSortednessLoanAmount.csv")

#sortednessMeasure(reverseSorted, array, 2,1, "SelectionSortMemorySortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 2,2, "InsertionSortMemorySortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 2,3, "BubbleSortMemorySortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 2,4, "MergeSortMemorySortednessLoanAmount.csv")
#sortednessMeasure(reverseSorted, array, 2,5, "QuickSortMemorySortednessLoanAmount.csv")


array = helpers.getArray(10, "SyntheticDataset.csv")
array = sort.quickSort(array, 0, len(array)-1)
reverseSorted = array.copy();
reverseSorted.reverse();

sortednessMeasure(reverseSorted, array, 1,1, "SelectionSortTimeSortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 1,2, "InsertionSortTimeSortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 1,3, "BubbleSortTimeSortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 1,4, "MergeSortTimeSortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 1,5, "QuickSortTimeSortednessSynthetic.csv")

#sortednessMeasure(reverseSorted, array, 2,1, "SelectionSortMemorySortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 2,2, "InsertionSortMemorySortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 2,3, "BubbleSortMemorySortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 2,4, "MergeSortMemorySortednessSynthetic.csv")
#sortednessMeasure(reverseSorted, array, 2,5, "QuickSortMemorySortednessSynthetic.csv")

