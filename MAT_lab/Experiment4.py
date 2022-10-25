#write a program to compute mean median mode and standard deviation of the given data using python.
from tkinter import N
from numpy import sort

from macpath import join
#----------------------------------------------------------------Mean------------------------------------------------------------------------
x = [1,2,3,4,5,6,7]
Add = 1+2+3+4+5+6+7
print("sum is :",Add)
length=len(x)
Mean= Add/length
print(Mean)

#----------------------------------------------------------------Median---------------------------------------------------------------------
num = [1, 2, 3, 4, 5]
num_length = len(num)
num.sort()
  
if num_length % 2 == 0:
    median1 = num[num_length//2]
    median2 = num[num_length//2 - 1]
    median = (median1 + median2)/2
else:
    median = num[num_length//2]
print("Median is: " + str(median))

#-----------------------------------------------------------------Mode--------------------------------------------------------------------
from collections import Counter
data = Counter(num)
getmode = dict(data)
mode = [k for k, v in getmode.items()if v == max(list(data.values()))]
if len(mode)==num_length:
   getmode = "No mode found"
else:
   getmode = "Mode = "+ ','.join(map(str, mode))
print(getmode)