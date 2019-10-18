#Mike Cresswell
#Sonia Xu
#Simulation Project

#SORTING TECHNIQUES to implement:
# Selection Sort
# Merge sort
# Quick sort
# Finished: Bubble sort, Insertion sort

import plotly
import copy
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

def main():
    ogdata = [5,4,3,2,1]
    testdata = [5,4,3,2,1]
    display = bubblesort(copy.deepcopy(testdata))
    insertsortdisplay = insertionsort(copy.deepcopy(testdata))
    xaxis = [0,1,2,3,4,5]
    print(display)
    print(testdata)
    print(insertsortdisplay)
    #EXAMPLE GRAPH
    # fig.add_trace(go.Scatter(x=xaxis, y=display, name='bubblesort',
    #                      line=dict(color='aquamarine', width=4)))
    # fig.add_trace(go.Scatter(x=xaxis, y=ogdata, name='ogcopy',
    #                      line=dict(color='blue', width=4)))
    # fig.show()

    #CREATE 16 GRAPHS
    # fig = go.Figure()
    # fig = make_subplots(rows=8, cols=2, start_cell="bottom-left")

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6], name="test1nameee", line=dict(color='aquamarine', width=4)),
    #             row=1, col=1)

    # fig.add_trace(go.Scatter(x=[10, 11, 12], y=[4, 5, 6]),
    #             row=1, col=1)
                
    # fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    #             row=1, col=2)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=2, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=2, col=2)

    # fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    #             row=3, col=1)
                
    # fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    #             row=3, col=2)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=4, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=4, col=2)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=5, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=5, col=2)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=6, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=6, col=2)
    
    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=7, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=7, col=2)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6], name="test1nameee", 
    #             line=dict(color='aquamarine', width=3)),
    #             row=8, col=1)

    # fig.add_trace(go.Scatter(x=display, y=[4, 5, 6]),
    #             row=8, col=2)

    # fig.update_layout(height=2000, width=1100, title_text="Subplots")

    # fig.show()

def bubblesort(list):
    listlength = len(list)
    for n in range(listlength):
        for k in range(listlength-n-1):
            if list[k] > list[k+1]:
                temp = list[k+1]
                list[k+1] = list[k]
                list[k] = temp
    return list

def insertionsort(list):
    for i in range(1, len(list)): 
        key = list[i] 
        j = i-1
        while j >=0 and key < list[j] : 
            list[j+1] = list[j] 
            j -= 1
        list[j+1] = key 
    return list

main()