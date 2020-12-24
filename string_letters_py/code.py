#!/usr/bin/env python
# coding: utf-8

# In[24]:


def find_words(words_list,letters):
    dict_ = {}
    count = []
    l = 0;
    for i in words_list:
        c= 0
        for j in i:
            
            for letter in letters:
                if(j == letter):
                    c = c+1
        count .append(c)
    dict_ = dict(zip(words_list,count))
    return dict_
k = find_words(["TOE","POT","PUT"],"AEOPT")
print(k)


# In[14]:


letters = "abcd"
print(len(letters))


# In[ ]:




