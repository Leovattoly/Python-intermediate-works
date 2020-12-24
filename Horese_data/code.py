#!/usr/bin/env python
# coding: utf-8

# In[1]:


# inserting data 
import pandas as pd
df = pd.read_csv("horse (1).csv")
df.head(3)


# In[2]:


df.isnull().sum()


# In[4]:


import seaborn as sns
sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis")


# In[5]:


df.dropna(inplace=True)


# In[6]:


sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis")


# In[8]:


surgery = pd.get_dummies(df['surgery'],drop_first=True) # 0 for false
surgery.head(5)


# In[9]:


df.head()


# In[11]:


age = pd.get_dummies(df['age'],drop_first=True)


# In[12]:


temp_of_extremities = pd.get_dummies(df['temp_of_extremities'],drop_first=True)


# In[13]:


peripheral_pulse = pd.get_dummies(df['peripheral_pulse'],drop_first=True) 


# In[16]:


df.isnull().sum()


# In[17]:


mucous_membrane = pd.get_dummies(df['mucous_membrane'],drop_first=True) 
capillary_refill_time = pd.get_dummies(df['capillary_refill_time'],drop_first=True) 
pain = pd.get_dummies(df['pain'],drop_first=True) 
peristalsis = pd.get_dummies(df['peristalsis'],drop_first=True) 
abdominal_distention = pd.get_dummies(df['abdominal_distention'],drop_first=True) 
nasogastric_tube = pd.get_dummies(df['nasogastric_tube'],drop_first=True) 

#################################
nasogastric_reflux = pd.get_dummies(df['nasogastric_reflux'],drop_first=True) 
nasogastric_reflux_ph = pd.get_dummies(df['nasogastric_reflux_ph'],drop_first=True) 
rectal_exam_feces = pd.get_dummies(df['rectal_exam_feces'],drop_first=True) 
abdomen = pd.get_dummies(df['abdomen'],drop_first=True) 
abdomo_appearance = pd.get_dummies(df['abdomo_appearance'],drop_first=True) 

#######################

outcome = pd.get_dummies(df['outcome'],drop_first=True) 
surgical_lesion = pd.get_dummies(df['surgical_lesion'],drop_first=True) 
cp_data = pd.get_dummies(df['cp_data'],drop_first=True) 


# In[35]:


print(outcome)


# In[20]:


df = pd.concat([df,surgery,age,temp_of_extremities,peripheral_pulse,mucous_membrane,capillary_refill_time,pain,peristalsis,abdominal_distention,nasogastric_tube,nasogastric_reflux,nasogastric_reflux_ph,rectal_exam_feces,abdomen,abdomo_appearance,outcome,surgical_lesion,cp_data],axis=1)


# In[24]:


df.drop(['surgery','age','temp_of_extremities','peripheral_pulse','mucous_membrane','capillary_refill_time','pain','peristalsis','abdominal_distention','nasogastric_tube','nasogastric_reflux','nasogastric_reflux_ph','rectal_exam_feces','abdomen','abdomo_appearance','outcome','surgical_lesion','cp_data'],axis=1,inplace=True)


# In[25]:


df.head()


# In[26]:


#iv).Fit a decision tree classifier and observe the accuracy.

from sklearn.model_selection import train_test_split
train_data,test_data = train_test_split(df,test_size = 0.2,random_state = 100)


# In[41]:


df.isnull().sum()


# In[42]:


x_train = train_data.iloc[:,0:34].values
y_train = train_data.iloc[:,35].values


# In[44]:


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth = 2,random_state = 0)
clf.fit(x_train, y_train)


# In[45]:


x_test = train_data.iloc[:,0:34].values
y_test = train_data.iloc[:,35].values


# In[46]:


# The score method returns the accuracy of the model
score = clf.score(x_test, y_test)
print(score)


# In[47]:


#v).Fit a random forest classifier and observe the accuracy.

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(x_train,y_train)


# In[48]:


y_pred=clf.predict(x_test)


# In[49]:


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[ ]:




