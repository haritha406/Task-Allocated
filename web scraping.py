#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# In[ ]:


url = 'https://clinicaltrials.gov/ct2/results?cond='
condition=input("enter the disease")
URL=url+condition+'&term=&cntry=&state=&city=&dist='
print(URL)
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
soup


# In[ ]:


rows = soup.find_all('tr')
len(rows)


# In[51]:


# In[16]:


import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)


# In[52]:


df = pd.DataFrame(list_rows)
df.head(10)


# In[53]:


# In[17]:


df1 = df[0].str.split(',', expand=True)
df1.head(10)


# In[ ]:




