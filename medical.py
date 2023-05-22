#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


data=pd.read_csv("medical_examination.csv",header=0)
data.head()


# In[30]:


data.describe()


# In[31]:


data["height_meter"]=data["height"]/100


# In[32]:


del data["height"]


# In[33]:


overweight=data["weight"]/((data["height_meter"])*(data["height_meter"]))


# In[34]:


overweight.head()


# In[35]:


data.head()


# In[36]:


overweight=overweight>25
        


# In[37]:


overweight.head()


# In[42]:


overweight=overweight.astype(int)


# In[43]:


overweight.head()


# In[45]:


data["over_weight"]=overweight


# In[46]:


data.head()


# In[53]:


data["cholestrol"]=data["cholesterol"]>1


# In[54]:


data["cholestrol"]=data["cholestrol"].astype(int)


# In[55]:


data["cholestrol"].head()


# In[59]:


sns.catplot(data["cardio"])


# In[60]:


sns.heatmap(data)


# In[ ]:





# In[ ]:





# In[ ]:




