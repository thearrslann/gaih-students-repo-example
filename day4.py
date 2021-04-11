#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=0
liste=[]

while n<5:
    name= input("İsim: ")

    not1 = int(input("Not1: "))

    not2 = int(input("Not2: "))

    not3 = int(input("Not3: "))

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)



    kişi ={
        "ad":name,
        "not 1":not1,
        "not 2":not2,
        "not 3":not3,
        "son not":son_not
    }

    liste.append(kişi)
    n+=1
print(liste)


# In[ ]:




