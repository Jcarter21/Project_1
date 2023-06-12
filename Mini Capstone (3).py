#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[13]:


import numpy as np


# In[3]:


df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv
')


# In[6]:





# In[7]:


df.head()


# In[8]:


df.columns


# In[9]:


df.index


# In[10]:


df.info


# In[11]:


df.loc[(df['School DBN']=='02M416') & (df['Mean Score'])]


# In[12]:


df.tail()


# In[14]:


df.loc[(df['School DBN']== '02M416') & (df['Year']== 2017) & (df['Regents Exam']== 'Common Core Algebra'), 
       ['School DBN','School Name','Year', 'Regents Exam', 'Mean Score']]


# In[26]:


drop_cols = ['Number Scoring Below 70',
       'Percent Scoring Below 70', 'Number Scoring 70 or Above',
       'Percent Scoring 70 or Above', 'Number Scoring 80 or Above',
       'Percent Scoring 80 or Above', 'Number Scoring CR',
       'Percent Scoring CR']


# In[20]:


df.drop(drop_cols, inplace =True, axis=1)


# In[21]:


df.head()


# In[22]:


df.isnull()


# In[23]:


df.loc[(df['School DBN']== '02M416') & (df['Year']== 2017) & (df['Regents Exam']== 'Common Core Algebra'), 
       ['School DBN','School Name','Year', 'Regents Exam', 'Mean Score']]


# In[24]:



df.loc[(df['School DBN']== '02M416') & (df['Year']== 2016) & (df['Regents Exam']== 'Common Core Algebra'), 
       ['School DBN','School Name','Year', 'Regents Exam', 'Mean Score']].mean()


# In[25]:


df.plot()


# In[ ]:




