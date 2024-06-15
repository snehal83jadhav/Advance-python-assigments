#!/usr/bin/env python
# coding: utf-8
1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
2. Write a Python Program to Find Factorial of Number Using Recursion?
3. Write a Python Program to calculate your Body Mass Index?
4. Write a Python Program to calculate the natural logarithm of any number?
5. Write a Python Program for cube sum of first n natural numbers?
# In[3]:


#Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[5]:


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 5

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
    


# In[6]:


# BMI = weight / Height * height

h = float(input("enter your height in feet : "))
w = float(input("enter your weight in kilo : "))

bmi = w/(h**2)

print("The BIM is = ",bmi)


# In[7]:


# natural log of any no.
import math
x = int(input(("Enter a number : ")))
log = math.log(x)
print("Log of {} is {}".format(x, log))


# In[8]:


# sum of cube of n numbers
n = int(input("Enter n : "))
sum = 0
for i in range(1,n+1):
    sum+=i**3
print("Cube sum of {} natural numbers is {}".format(n,sum))


# In[ ]:




