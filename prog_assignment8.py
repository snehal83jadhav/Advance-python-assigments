#!/usr/bin/env python
# coding: utf-8
1. Write a Python Program to Add Two Matrices?
2. Write a Python Program to Multiply Two Matrices?
3. Write a Python Program to Transpose a Matrix?
4. Write a Python Program to Sort Words in Alphabetic Order?
5. Write a Python Program to Remove Punctuation From a String?
# In[2]:


#1. Write a Python Program to Add Two Matrices?
import numpy as np

mat1 = np.array([[1,6,4],
        [4,5,6],
        [7,6,9]])
mat2 = np.array([[2,5,4],
        [5,8,7],
        [8,3,1]])

sumMat = np.add(mat1,mat2)
print("The Sum of two matrix \n\n{}  and \n\n{}  is \n\n{} ".format(mat1,mat2,sumMat))


# In[3]:


#2. Write a Python Program to Multiply Two Matrices?
import numpy as np

mat1 = np.array([[1,2,4],
        [4,5,6],
        [7,8,9]])
mat2 = np.array([[2,3,4],
        [5,6,7],
        [8,9,1]])

sumMat = np.dot(mat1,mat2)
print("The product of two matrix \n\n{}  and \n\n{}  is \n\n{} ".format(mat1,mat2,sumMat))


# In[4]:


# 3. Write a Python Program to Transpose a Matrix?

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)


# In[4]:


# 4. Write a Python Program to Sort Words in Alphabetic Order?
str = input("Enter some string: ")

words = str.split()
words.sort()
for word in words:
    print(word)


# In[5]:


# 5. Write a Python Program to Remove Punctuation From a String?
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = input("Enter some string with panctuations")

# remove punctuation from the string
no_punct = ""
for char in str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# In[ ]:





# In[ ]:




