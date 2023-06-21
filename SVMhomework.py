#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot


# In[3]:


boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
boston_df=pd.read_csv(boston_url)


# For the "Median value of owner-occupied homes" provide a boxplot
# 
# Provide a  bar plot for the Charles river variable
# 
# Provide a boxplot for the MEDV variable vs the AGE variable. (Discretize the age variable into three groups of 35 years and younger, between 35 and 70 years and 70 years and older)
# 
# Provide a scatter plot to show the relationship between Nitric oxide concentrations and the proportion of non-retail business acres per town. What can you say about the relationship?

# In[6]:


ax = sns.barplot(x="CHAS", y="MEDV", data=boston_df)


# In[11]:


ax = sns.boxplot(y='MEDV', data=boston_df)


# In[12]:


ax = sns.scatterplot(x='NOX', y='INDUS', data=boston_df)


# In[ ]:




