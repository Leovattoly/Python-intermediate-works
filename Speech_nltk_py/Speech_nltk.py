#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk

nltk.download('inaugural')

from nltk.corpus import inaugural

inaugural.fileids()

Roosevelt = inaugural.raw('1941-Roosevelt.txt')

Kennedy = inaugural.raw('1961-Kennedy.txt')

Nixon = inaugural.raw('1973-Nixon.txt')


# In[10]:


#get the length of the data
number_of_characters = len(Roosevelt)

print('Number of characters in Roosevelt file :', number_of_characters)

number_of_characters = len(Kennedy)

print('Number of characters in Kennedy file :', number_of_characters)

number_of_characters = len(Nixon)

print('Number of characters in Nixon file :', number_of_characters)


# In[13]:


from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter

tokenizer = RegexpTokenizer(r'\w+')
Roosevelt_no_punc = tokenizer.tokenize(Roosevelt)
set(w.title() for w in Roosevelt_no_punc if w.lower() not in stopwords.words())
word_count_dict = Counter(w.title() for w in zen_no_punc if w.lower() not in stopwords.words())
word_count_dict.most_common()


# In[14]:


# Remove all the stopwords from the Roosevelt speeches.

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(Roosevelt) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 


# In[ ]:


# Remove all the stopwords from the Kennedy speeches.


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(Kennedy) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 


# In[ ]:


# Remove all the stopwords from the Nixon speeches.


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(Nixon) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 

