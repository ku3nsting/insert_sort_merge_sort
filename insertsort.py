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

# insertion sort implementation
# used as reference: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def insertSort(sortData):
   for index in range(1, len(sortData)):  #dpn't bother iterating over 0 index because the sort operation always looks one index lower than current value

     currentvalue = sortData[index]
     position = index

     while position > 0 and sortData[position-1] > currentvalue:
         sortData[position] = sortData[position-1]
         position = position-1

     sortData[position] = currentvalue

#start timer
# reference: https://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
executionStart = time.time()

timeList = []

for x in range(20):
	print(x + 1)
	insertSort(sortData)
	print(sortData)
	timeDiff = time.time() - executionStart
	print("Insert Sort time:")
	print("--- "+str(timeDiff)+ " ---");
	timeList.append(timeDiff)
	
totalTime = 0;
for each in range(sortNum):
	totalTime = totalTime + timeList[each]
	
timeAvg = totalTime / sortNum
print("AVERAGE Sort time:")
print("--- "+str(timeAvg)+ " ---");
        
