#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import numpy as np
import pandas as pd
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split
from sklearn import model_selection 


# In[4]:


data1 = pd.read_csv('car.data',names=['buying','maint','doors','persons','lug_boot','safety','class'])


# In[5]:


data1.head()


# In[6]:


data1.info()


# In[7]:


data1['class'],class_names = pd.factorize(data1['class'])


# In[9]:


print(class_names)
print(data1['class'].unique())


# In[11]:


data1['buying'],_ = pd.factorize(data1['buying'])
data1['maint'],_ = pd.factorize(data1['maint'])
data1['doors'],_ = pd.factorize(data1['doors'])
data1['persons'],_ = pd.factorize(data1['persons'])
data1['lug_boot'],_ = pd.factorize(data1['lug_boot'])
data1['safety'],_ = pd.factorize(data1['safety'])
data1.head()


# In[13]:


data1.info()                       #all are converted to integers


# In[14]:


X = data1.iloc[:,:-1]
y = data1.iloc[:,-1]


# In[21]:


# split data randomly into 70% training and 30% test
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)


# In[22]:


# train the decision tree
dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
dtree.fit(X_train, y_train)


# In[23]:


# use the model to make predictions with the test data
y_pred = dtree.predict(X_test)
# how did our model perform?
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))


# In[27]:


import graphviz


# In[28]:


feature_names = X.columns

dot_data = tree.export_graphviz(dtree, out_file=None, filled=True, rounded=True,
                                feature_names=feature_names,  
                                class_names=class_names)
graph = graphviz.Source(dot_data)  
graph


# In[ ]:




