#!/usr/bin/env python 

#importing packages
import time

#get the data
with open("data.txt") as file:
    dataArray = []
    for line in file:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            dataArray.append(line)

sortData = dataArray[1]
sortNum = dataArray[0]
sortNum = sortNum[0]

print("Number of values to sort: " + str(sortNum))
print("Starting list: " + str(sortData))

sublist = []
for i in range(sortNum):
        sublist.append(sortData[i])

sortData = sublist

# Merge sort implementation
# used as reference: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(sortData):
    if len(sortData) > 1:
        middle = len(sortData)/ 2
        lefthalf = sortData[:middle]  #equivalent of "beginning to the middle"
        righthalf = sortData[middle:] #equivalent of "middle to end"

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
		
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sortData[k] = lefthalf[i]
                i = i+1
            else:
                sortData[k] = righthalf[j]
                j = j+1
            k=k+1

        while i < len(lefthalf):
            sortData[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            sortData[k] = righthalf[j]
            j = j+1
            k = k+1

#start timer
# reference: https://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
executionStart = time.time()

mergeSort(sortData)
print(sortData)
        
print("Merging time:")
print("--- %s seconds ---" % (time.time() - executionStart))
        
