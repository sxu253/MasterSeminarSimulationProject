import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
import numpy as np
import pandas as pd
import seaborn as sns
import pylab as plt

def SyntheticMemorybySortedness():
    bubbleSort = pd.read_csv('BubbleSortMemorySortedness.csv')
    bubbleMean = bubbleSort.mean(axis = 0)

    insertionSort = pd.read_csv('InsertionSortMemorySortedness.csv')
    insertionMean = insertionSort.mean(axis = 0)

    mergeSort = pd.read_csv('MergeSortMemorySortedness.csv')
    mergeMean = mergeSort.mean(axis = 0)

    quickSort = pd.read_csv('QuickSortMemorySortedness.csv')
    quickMean = quickSort.mean(axis = 0)

    selectionSort = pd.read_csv('SelectionSortMemorySortedness.csv')
    selectionMean = selectionSort.mean(axis = 0)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Synthetic Memory by Sortedness')
    plt.ylabel('Memory')
    plt.xlabel('Sortedness')
    plt.legend();
    plt.savefig('Synthetic_Memory_Sortedness.png')
    plt.show()


def LoanAmountMemorybySortedness():
    bubbleSort = pd.read_csv('BubbleSortMemorySortednessLoanAmount.csv')
    bubbleMean = bubbleSort.mean(axis = 0)

    insertionSort = pd.read_csv('InsertionSortMemorySortednessLoanAmount.csv')
    insertionMean = insertionSort.mean(axis = 0)

    mergeSort = pd.read_csv('MergeSortMemorySortednessLoanAmount.csv')
    mergeMean = mergeSort.mean(axis = 0)

    quickSort = pd.read_csv('QuickSortMemorySortednessLoanAmount.csv')
    quickMean = quickSort.mean(axis = 0)

    selectionSort = pd.read_csv('SelectionSortMemorySortednessLoanAmount.csv')
    selectionMean = selectionSort.mean(axis = 0)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Loan Amount Memory by Sortedness')
    plt.ylabel('Memory')
    plt.xlabel('Sortedness')
    plt.legend();
    plt.savefig('LoanAmount_Memory_Sortedness.png')
    plt.show()

def SyntheticTimebySortedness():
    bubbleSort = pd.read_csv('BubbleSortTimeSortedness.csv')
    bubbleMean = bubbleSort.mean(axis = 0)

    insertionSort = pd.read_csv('InsertionSortTimeSortedness.csv')
    insertionMean = insertionSort.mean(axis = 0)

    mergeSort = pd.read_csv('MergeSortTimeSortedness.csv')
    mergeMean = mergeSort.mean(axis = 0)

    quickSort = pd.read_csv('QuickSortTimeSortedness.csv')
    quickMean = quickSort.mean(axis = 0)

    selectionSort = pd.read_csv('SelectionSortTimeSortedness.csv')
    selectionMean = selectionSort.mean(axis = 0)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Synthetic Time by Sortedness')
    plt.ylabel('Time')
    plt.xlabel('Sortedness')
    plt.legend();
    plt.savefig('Synthetic_Time_Sortedness.png')
    plt.show()

def LoanAmountTimebySortedness():
    bubbleSort = pd.read_csv('BubbleSortTimeSortednessLoanAmount.csv')
    bubbleMean = bubbleSort.mean(axis = 0)

    insertionSort = pd.read_csv('InsertionSortTimeSortednessLoanAmount.csv')
    insertionMean = insertionSort.mean(axis = 0)

    mergeSort = pd.read_csv('MergeSortTimeSortednessLoanAmount.csv')
    mergeMean = mergeSort.mean(axis = 0)

    quickSort = pd.read_csv('QuickSortTimeSortednessLoanAmount.csv')
    quickMean = quickSort.mean(axis = 0)

    selectionSort = pd.read_csv('SelectionSortTimeSortednessLoanAmount.csv')
    selectionMean = selectionSort.mean(axis = 0)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    x1 = np.linspace(0.0, 5.0)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Loan Amount Time by Sortedness')
    plt.ylabel('Time')
    plt.xlabel('Sortedness')
    plt.legend();
    plt.savefig('LoanAmount_Time_Sortedness.png')
    plt.show()


def SyntheticMemorybySize():
    bubbleSort = pd.read_csv('SyntheticBubbleSortMemory.csv')
    bubbleMean = bubbleSort.mean(axis = 1)

    insertionSort = pd.read_csv('SyntheticInsertionSortMemory.csv')
    insertionMean = insertionSort.mean(axis = 1)

    mergeSort = pd.read_csv('SyntheticMergeSortMemory.csv')
    mergeMean = mergeSort.mean(axis = 1)

    quickSort = pd.read_csv('SyntheticQuickSortMemory.csv')
    quickMean = quickSort.mean(axis = 1)

    selectionSort = pd.read_csv('SyntheticSelectionSortMemory.csv')
    selectionMean = selectionSort.mean(axis = 1)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    x1 = np.linspace(0.0, 5.0)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Synthetic Memory by Size')
    plt.ylabel('Memory')
    plt.xlabel('Size')
    plt.legend();
    plt.savefig('Synthetic_Memory_Size.png')
    plt.show()

def LoanAmountMemorybySize():
    bubbleSort = pd.read_csv('LoanBubbleSortMemory.csv')
    bubbleMean = bubbleSort.mean(axis = 1)

    insertionSort = pd.read_csv('LoanInsertionSortMemory.csv')
    insertionMean = insertionSort.mean(axis = 1)

    mergeSort = pd.read_csv('LoanMergeSortMemory.csv')
    mergeMean = mergeSort.mean(axis = 1)

    quickSort = pd.read_csv('LoanQuickSortMemory.csv')
    quickMean = quickSort.mean(axis = 1)

    selectionSort = pd.read_csv('LoanSelectionSortMemory.csv')
    selectionMean = selectionSort.mean(axis = 1)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    x1 = np.linspace(0.0, 5.0)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Loan Amount Memory by Size')
    plt.ylabel('Memory')
    plt.xlabel('Size')
    plt.legend();
    plt.savefig('LoanAmount_Memory_Size.png')
    plt.show()

def SyntheticTimebySize():
    bubbleSort = pd.read_csv('SyntheticBubbleSortTimes.csv')
    bubbleMean = bubbleSort.mean(axis = 1)

    insertionSort = pd.read_csv('SyntheticInsertionSortTimes.csv')
    insertionMean = insertionSort.mean(axis = 1)

    mergeSort = pd.read_csv('SyntheticMergeSortTimes.csv')
    mergeMean = mergeSort.mean(axis = 1)

    quickSort = pd.read_csv('SyntheticQuickSortTimes.csv')
    quickMean = quickSort.mean(axis = 1)

    selectionSort = pd.read_csv('SyntheticSelectionSortTimes.csv')
    selectionMean = selectionSort.mean(axis = 1)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    x1 = np.linspace(0.0, 5.0)
    ax1.scatter(selectionMean.index, selectionMean, c='b', label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', label='Quick')
    plt.title('Synthetic Time by Size')
    plt.ylabel('Time')
    plt.xlabel('Size')
    plt.legend();
    plt.savefig('Synthetic_Time_Size.png')
    plt.show()

def LoanAmountbySize():
    bubbleSort = pd.read_csv('LoanBubbleSort.csv')
    bubbleMean = bubbleSort.mean(axis = 1)

    insertionSort = pd.read_csv('LoanInsertionSort.csv')
    insertionMean = insertionSort.mean(axis = 1)

    mergeSort = pd.read_csv('LoanMergeSort.csv')
    mergeMean = mergeSort.mean(axis = 1)

    quickSort = pd.read_csv('LoanQuickSort.csv')
    quickMean = quickSort.mean(axis = 1)

    selectionSort = pd.read_csv('LoanSelectionSort.csv')
    selectionMean = selectionSort.mean(axis = 1)

    fig1 = plt.figure(figsize=(30,15))
    ax1 = fig1.add_subplot(111)
    x1 = np.linspace(0.0, 5.0)
    ax1.scatter(selectionMean.index, selectionMean, c='b', marker="o", label='Selection')
    ax1.scatter(bubbleMean.index, bubbleMean,  c='r', marker="o", label='Bubble')
    ax1.scatter(insertionMean.index, insertionMean, c='g', marker="o", label='Insertion')
    ax1.scatter(mergeMean.index, mergeMean,  c='y', marker="o", label='Merge')
    ax1.scatter(quickMean.index, quickMean, c='k', marker="o", label='Quick')
    plt.title('Loan Amount Time by Size')
    plt.ylabel('Time')
    plt.xlabel('Size')
    plt.legend();
    plt.savefig('LoanAmount_Time_Size.png')
    plt.show()

SyntheticMemorybySortedness()
SyntheticTimebySortedness()
SyntheticMemorybySize()
SyntheticTimebySize()

LoanAmountMemorybySize()
LoanAmountbySize()
LoanAmountTimebySortedness()
LoanAmountMemorybySortedness()