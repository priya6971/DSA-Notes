# -*- coding: utf-8 -*-
"""sort012.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rn-soRDWsR91TqmccufoysIxTrQCijq7

# Problem Statement - 
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Note that you cannot use any sorting algorithm to implement above code.
##
Input: 
N = 5
arr[]= {0 2 1 2 0}
##
Output:
0 0 1 2 2
##
Expected Time Complexity: O(N)
##
Expected Auxiliary Space: O(1)
"""

def sort012(a,n):
  j = 0
  # to get 0's ahead
  for i in range(n):
    if (a[i] == 0):
      if (i == j):
        j = j + 1
      else:
        # Swap of a[i] and a[j]
        a[i],a[j] = a[j],a[i]
        j = j + 1
  # to get 1's after 0's
  i = j
  for i in range(n):
    if (a[i] == 1):
      if (i == j):
        j = j + 1
      else:
        a[i],a[j] = a[j],a[i]
        j = j + 1
        
# Driver code
#n -> Number of elements in an array
n = int(input("Size of an array"))
A = []
for i in range(n):
  element = int(input("Enter the element"))
  A.append(element)

print(A)
sort012(A,n)
print(A)

