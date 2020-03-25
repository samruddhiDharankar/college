#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder


# In[2]:


df_census = pd.read_csv('adult.csv')


# In[30]:


dataset = pd.read_csv('WorldCupMatches.csv')


# In[19]:


df_census


# In[21]:


df_census.head(5)


# In[22]:


df_census.tail(5)


# In[23]:


df_census.shape


# In[24]:


df_census.index


# In[26]:


df_census.columns


# In[27]:


df_census.isnull()


# In[49]:


#Tuple Duplication


# In[4]:


bool_series = df_census.duplicated(subset=None, keep=False)
bool_series


# In[5]:


df_census_unique = df_census[~bool_series]
df_census_unique


# In[6]:


bool_series


# In[7]:


df_census.shape


# In[8]:


#after removing duplication
df_census_unique.shape


# In[9]:


#data integrity
dataset1 = pd.read_csv('adult.csv')
dataset2 = pd.read_csv('adult.csv')


# In[10]:


combined_dataset = pd.concat([dataset1,dataset2])


# In[11]:


combined_dataset.shape


# In[14]:


#histogram
data = pd.read_csv('diamonds.csv')

plt.hist(data.cut,orientation='vertical')
plt.title('cut histogram')
plt.xlabel('cut')
plt.ylabel('frequency')
cut = ('ideal','premium','good','very good','fair')
index = np.arange(len(cut))
#plt.sticks(index,cut,rotation=90)
plt.show()


# In[15]:


#correlation
data.corr()


# In[16]:


plt.matshow(data.corr())


# In[18]:


correlation_matrix = data.corr().round(2)
plt.show()
plt.savefig("heatmap.png")
plt.clf
plt.close()


# In[31]:


dataset


# In[32]:


dataset.tail(6)


# In[33]:


dataset.shape


# In[34]:


dataset.isnull()


# In[36]:


dataset.isnull().sum()


# In[37]:


dataset.dropna(inplace=True)


# In[38]:


dataset.isnull().sum()


# In[39]:


dataset.shape


# In[40]:


dataset.tail()


# In[41]:


dataset['Year'].tail()


# In[42]:


dataset['Year'].mean()


# In[43]:


dataset['Year'].replace(np.NaN,dataset['Year'].mean())


# In[44]:


x = dataset.iloc[-1:,:-1].values


# In[45]:


x


# In[46]:


label_encoder = LabelEncoder()


# In[48]:


x[:, 0] = label_encoder.fit_transform(x[:,0])
x


# In[50]:


dataset.columns


# In[59]:


#pearsonr correlation
import scipy
from scipy.stats.stats import pearsonr


# In[64]:


year = dataset['Year']
attendance = dataset['Attendance']
roundid = dataset['RoundID']
matchid = dataset['MatchID']


# In[60]:


pearsonr_coefficient,p_value = pearsonr(year,attendance)
print ("pearsonr coefficient %0.3f",pearsonr_coefficient)


# In[63]:


pearsonr_coefficient,p_value = pearsonr(year,roundid)
print ("pearsonr coefficient %0.3f",pearsonr_coefficient)


# In[65]:


pearsonr_coefficient,p_value = pearsonr(year,matchid)
print ("pearsonr coefficient %0.3f",pearsonr_coefficient)


# In[82]:


X = dataset[['Year','Attendance','RoundID','MatchID']]


# In[83]:


corr = X.corr()
corr


# In[84]:


sns.heatmap(corr,xticklabels=corr.columns.values,yticklabels=corr.columns.values)


# In[85]:


#data transformation
data


# In[88]:


data["cut"]=data["cut"].str.upper()


# In[89]:


data


# In[92]:


#Normalization
price = data.price
normalized = (price-price.min())/(price.max()-price.min())


# In[93]:


normalized


# In[99]:


#z-score normalization
from scipy.stats import zscore


# In[105]:


data['zscore'] = (data.price - data.price.mean())/data.price.std(ddof=0)


# In[107]:


dataset1.to_excel("Z-Scores.xlsx")


# In[109]:


data


# In[ ]:




