#!/usr/bin/env python
# coding: utf-8

# In[1]:


#how many nucleiotides are present
#How many persentage of GC content 
#purine base persentage 
#Pyrimidine base percentages 


# In[6]:


DNA="AGTTAGCTAGGAG"
length=len(DNA)
print(length)


# In[19]:


G_count=DNA.count("G")
C_count=DNA.count("C")
T_count=DNA.count("T")
A_count=DNA.count("A")
GC_count=G_count + C_count/length*100
print(GC_count)


# In[31]:


purine_base_count=G_count+A_count
pyrimidine_base_count=C_count+T_count
Puranie_base=G_count+A_count/length*100
pyrimidine_base=C_count+T_count/length*100
print("purine base count is:",purine_base_count)
print("pyrimidine base count is:",pyrimidine_base_count)
print("purine base is:",Puranie_base)
print("pyrimindine base is:",pyrimidine_base)


# In[ ]:




