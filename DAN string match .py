#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#this progrsm will give you a reverse complimentory to the given sequence 
compliment={'A':'T','C':'G','T':'A','G':'C'}
def reverseComplimentory(s):
    complimentory={'A':'T','C':'G','T':'A','G':'C'}
    d=""
    for base in (s):
        d=compliment[base]+d
    return d   
reverseComplimentory(input("Enter string:"))
    


# In[ ]:





# In[ ]:





# In[ ]:




