#!/usr/bin/env python
# coding: utf-8

# In[59]:


listem=[1,2,3,4,5,6,7,8,9,10]
orta= int(len(listem)/2)
birinci= listem[:orta]
ikinci= listem[orta:]
ikinci.extend(birinci)
print(ikinci)

