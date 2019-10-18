

import numpy as np
import pandas as pd
import seaborn as sns
import csv
import time
import tracemalloc
from scipy import stats


def insertionSort(array): 
    for i in range(1, len(array)): 
        item = array[i]
        j = i-1
        while j >= 0 and item < array[j]: 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = item 


def selectionSort(array):
    for i in range(len(array)): 
        min = i 
        for j in range(i+1, len(array)): 
            if array[min] > array[j]: 
                min = j 
      
        array[i], array[min] = array[min], array[i] 


def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]


def mergeSort(array): 
    if len(array) > 1: 
        Middle = len(array)//2 
        Left = array[:Middle]
        Right = array[Middle:] 
  
        mergeSort(Left) 
        mergeSort(Right)
  
        i = j = k = 0
        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: 
                array[k] = Left[i] 
                i+=1
            else: 
                array[k] = Right[j] 
                j+=1
            k+=1

        while i < len(Left): 
            array[k] = Left[i] 
            i+=1
            k+=1
          
        while j < len(Right): 
            array[k] = Right[j] 
            j+=1
            k+=1

def partition(array,low,high): 
    i = (low-1)         
    pivot = array[high]     
    for j in range(low , high): 
        if   array[j] < pivot: 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[high] = array[high],array[i+1] 
    return ( i+1 ) 

  
def quickSort(array,low,high): 
    if low < high: 
        pi = partition(array,low,high) 
        quickSort(array, low, pi-1) 
        quickSort(array, pi+1, high) 


#takes number of elements to read from file
def getArray(size, fileName): 
    my_list = []
    i = 0
    with open(fileName, newline='') as f:
      reader = csv.reader(f)
      for row in reader:  
        my_list.append(int(row[0]))
        i = i + 1
        if i >= size:
            break
    return my_list

#Still testing these, let me know if you find a bug
#run functions takes file name of dataset to read in, filename of measurements output and number of iterations
def runQuickSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = getArray(x, inputfileName)
            startTime = time.time()
            quickSort(array, 0, len(array)-1)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runInsertionSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = getArray(x, inputfileName)
            startTime = time.time()
            insertionSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runSelectionSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = getArray(x, inputfileName)
            startTime = time.time()
            selectionSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


def runBubbleSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = getArray(x, inputfileName)
            startTime = time.time()
            bubbleSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)



def runMergeSort(inputfileName, outputfileName ,iterations):
    times = [];
    for x in range(iterations):
        t = []
        for y in range(5):
            array = getArray(x, inputfileName)
            startTime = time.time()
            mergeSort(array)
            endTime = time.time()
            t.append(endTime - startTime)
        times.append(t)

    df =  pd.DataFrame(data=times, columns= ['1', '2', '3', '4', '5'])
    df.to_csv(index=False, sep=",", path_or_buf=outputfileName)


#driver functions for synthetic datasets and real world datasets
runQuickSort("SyntheticDataset.csv","SyntheticQuickSortTimes.csv",10)
runInsertionSort("SyntheticDataset.csv","SyntheticInsertionSortTimes.csv",10)
runSelectionSort("SyntheticDataset.csv","SyntheticSelectionSortTimes.csv",10)
runBubbleSort("SyntheticDataset.csv","SyntheticBubbleSortTimes.csv",10)
runMergeSort("SyntheticDataset.csv","SyntheticMergeSortTimes.csv",10)

runQuickSort("LoanAmountDataset.csv","LoanQuickSort.csv",10)
runInsertionSort("LoanAmountDataset.csv","LoanInsertionSort.csv",10)
runSelectionSort("LoanAmountDataset.csv","LoanSelectionSort.csv",10)
runBubbleSort("LoanAmountDataset.csv","LoanBubbleSort.csv",10)
runMergeSort("LoanAmountDataset.csv","LoanMergeSort.csv",10)