import numpy as np
import pandas as pd
import seaborn as sns
import csv
import time
import tracemalloc
from scipy import stats
import SortingFunctions as sort
import Helpers as helpers


def runMemoryInsertionSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            tracemalloc.start()
            sort.insertionSort(array)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runMemorySelectionSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            tracemalloc.start()
            sort.selectionSort(array)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)

def runMemoryBubbleSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            tracemalloc.start()
            sort.bubbleSort(array)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)

def runMemoryMergeSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            tracemalloc.start()
            sort.mergeSort(array)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)

def runMemoryQuickSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            tracemalloc.start()
            sort.quickSort(array,0,len(array)-1)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


#runMemoryMergeSort("SyntheticDataset.csv","SyntheticMergeSortMemory.csv",1000)
#runMemoryQuickSort("SyntheticDataset.csv","SyntheticQuickSortMemory.csv",1000)
#runMemoryInsertionSort("SyntheticDataset.csv","SyntheticInsertionSortMemory.csv",1000)
#runMemorySelectionSort("SyntheticDataset.csv","SyntheticSelectionSortMemory.csv",1000)
#runMemoryBubbleSort("SyntheticDataset.csv","SyntheticBubbleSortMemory.csv",1000)

#runMemoryMergeSort("LoanAmountDataset.csv","LoanMergeSortMemory.csv",1000)
#runMemoryQuickSort("LoanAmountDataset.csv","LoanQuickSortMemory.csv",1000)
#runMemoryInsertionSort("LoanAmountDataset.csv","LoanInsertionSortMemory.csv",1000)
#runMemorySelectionSort("LoanAmountDataset.csv","LoanSelectionSortMemory.csv",1000)
#runMemoryBubbleSort("LoanAmountDataset.csv","LoanBubbleSortMemory.csv",1000)