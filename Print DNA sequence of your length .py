#!/usr/bin/env python
# coding: utf-8

# In[44]:


#this code prove you with the random sequence with the length you want how much long sequence you want 
import random 
seq1=""
L = int(input("Enter number: "))
for _ in range(L):
    seq1= seq1 + random.choice("ATGC")
print(seq1)

