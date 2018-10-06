
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


Babynames = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')


# In[6]:


Babynames.head(6)


# In[9]:


Babynames.columns


# In[11]:


#Delete unnamed columns
Babynames.drop('Unnamed: 0',axis=1,inplace=True)


# In[12]:


Babynames.columns


# In[18]:


#Show the distribution of male and female
Babynames.Gender.dtype


# In[9]:


Babynames.groupby('Gender').describe()


# In[12]:


Babynames.loc[Babynames['Id'] == Babynames.loc[:,'Id'].median()]['Name']


# In[13]:



Babynames.groupby(['State','Gender']).Count.sum().reset_index(name='Count')

