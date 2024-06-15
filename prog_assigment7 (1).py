#!/usr/bin/env python
# coding: utf-8
1.Write a Python Program to find sum of array?
2. Write a Python Program to find largest element in an array?
3. Write a Python Program for array rotation?
4. Write a Python Program to Split the array and add the first part to the end?
5. Write a Python Program to check if given array is Monotonic?
# In[1]:


#Solution 1
lst = [1,2,3,4,5,6,7,8,9]
sum(lst)


# In[3]:


# largest element in an array
lst = [100,240,310,67,445,9]
max(lst)
print("lstgetst elemnt in the array {} is {}".format(lst,max(lst)))


# In[20]:


def rverseArray(arr,d):
    c=(arr[d:])+(arr[:d])
    return c
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
d=len(arr)-1
print(rverseArray(arr,d))


# In[1]:


# Python program to split array and move first part to end.
 
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
 
        arr[n-1] = x
 
 
# main
arr = [3, 4, 5, 6, 52, 36]
n = len(arr)
position = 2
 
splitArr(arr, n, position)
 
for i in range(0, n):
    print(arr[i], end=' ')


# In[2]:


n = int(input("Enter the length of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)

if all((lst[i] <= lst[i+1] for i in range(n-1)) or (lst[i] >= lst[i+1] for i in range(n-1))):
    print("Monotonic")
else:
    print("Not Monotonic")


# In[ ]:





# In[ ]:




