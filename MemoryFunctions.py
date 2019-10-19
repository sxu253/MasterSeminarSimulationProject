import numpy as np
import pandas as pd
import seaborn as sns
import csv
import time
import tracemalloc
from scipy import stats
import SortingFunctions as sort
import SortingSimulator as sim


def runMemoryInsertionSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = sim.getArray(x, inputfileName)
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
            array = sim.getArray(x, inputfileName)
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
            array = sim.getArray(x, inputfileName)
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
            array = sim.getArray(x, inputfileName)
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
            array = sim.getArray(x, inputfileName)
            tracemalloc.start()
            sort.quickSort(array,0,len(array)-1)
            cur, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            t.append(peak)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


runMemoryMergeSort("SyntheticDataset.csv","SyntheticMergeSortMemory.csv",100)
runMemoryQuickSort("SyntheticDataset.csv","SyntheticQuickSortMemory.csv",100)
runMemoryInsertionSort("SyntheticDataset.csv","SyntheticInsertionSortMemory.csv",100)
runMemorySelectionSort("SyntheticDataset.csv","SyntheticSelectionSortMemory.csv",100)
runMemoryBubbleSort("SyntheticDataset.csv","SyntheticBubbleSortMemory.csv",100)

runMemoryMergeSort("LoanAmountDataset.csv","LoanMergeSortMemory.csv",100)
runMemoryQuickSort("LoanAmountDataset.csv","LoanQuickSortMemory.csv",100)
runMemoryInsertionSort("LoanAmountDataset.csv","LoanInsertionSortMemory.csv",100)
runMemorySelectionSort("LoanAmountDataset.csv","LoanSelectionSortMemory.csv",100)
runMemoryBubbleSort("LoanAmountDataset.csv","LoanBubbleSortMemory.csv",100)