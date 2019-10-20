
import numpy as np
import pandas as pd
import seaborn as sns
import csv
import time
import tracemalloc
from scipy import stats
import Helpers as helpers
import SortingFunctions as sort


def runQuickSort(inputfileName, outputfileName, iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            startTime = time.time()
            sort.quickSort(array, 0, len(array)-1)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runInsertionSort(inputfileName, outputfileName, iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            startTime = time.time()
            sort.insertionSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runSelectionSort(inputfileName, outputfileName, iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            startTime = time.time()
            sort.selectionSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runBubbleSort(inputfileName, outputfileName, iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            startTime = time.time()
            sort.bubbleSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)



def runMergeSort(inputfileName, outputfileName, iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = helpers.getArray(x, inputfileName)
            startTime = time.time()
            sort.mergeSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)



runQuickSort("SyntheticDataset.csv","SyntheticQuickSortTimes.csv",10)
#runInsertionSort("SyntheticDataset.csv","SyntheticInsertionSortTimes.csv",1000)
#runSelectionSort("SyntheticDataset.csv","SyntheticSelectionSortTimes.csv",1000)
#runBubbleSort("SyntheticDataset.csv","SyntheticBubbleSortTimes.csv",1000)
#runMergeSort("SyntheticDataset.csv","SyntheticMergeSortTimes.csv",1000)

#runQuickSort("LoanAmountDataset.csv","LoanQuickSort.csv",1000)
#runInsertionSort("LoanAmountDataset.csv","LoanInsertionSort.csv",1000)
#runSelectionSort("LoanAmountDataset.csv","LoanSelectionSort.csv",1000)
#runBubbleSort("LoanAmountDataset.csv","LoanBubbleSort.csv",1000)
#runMergeSort("LoanAmountDataset.csv","LoanMergeSort.csv",1000)