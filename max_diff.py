'''
Maximum difference between two elements such that larger element appears after the smaller number

Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number. 

Examples : 

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
'''

def max_diff(arr):
    length=len(arr)
    
    minimum=arr[0]
    
    maxd=-1
    for i in range(1,length):
        if arr[i]>=minimum:
            maxd=max(maxd,arr[i]-minimum)
        elif arr[i]<minimum:
            minimum=arr[i]
            
    return maxd
