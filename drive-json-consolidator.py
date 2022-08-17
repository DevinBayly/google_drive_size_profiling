#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pathlib import Path
import pandas as pd
import json


# In[3]:


jsons = list(Path("./").rglob("*.json"))


# In[4]:


jsons


# structure that I want is, 
# 1 file per row, with a column that is named folder
# 
# 

# In[29]:


def aggregator(jfile,collect):
    print(jfile)
    try:
        jdict= json.loads(open(f"{jfile}").read())
        for row in jdict:
            row["FolderName"] = jfile.stem
        collect.extend(jdict)
    except Exception as e:
        print(e, jfile)
    
    


# In[30]:


res =[]
for j in jsons:
    aggregator(j,res)
    


# In[31]:


df = pd.DataFrame(res)

df.to_csv("drive_files_analyzed.csv")
    

