#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from csv import reader


# In[4]:


data=list(reader(open('mid_cleaned2.csv', encoding='utf-8')))
data


# In[5]:


data[0].index('CUSTOMER_TYPE')


# In[7]:


data[0].index('COUNTRY') ARTISTIC MILLINERS (AMG)


# In[25]:


for i in data[1:]:
    
    abc= i[23]
    print(i[6], abc, i[3])
    if not i[6]:
        if abc:
            if abc != 'Pakistan' and abc !='PAKISTAN':
        #         i[7]= 'Export'
                print('aa')
            elif (abc == 'PAKISTAN' or abc== 'Pakistan') and i[3]== 'ARTISTIC MILLINERS(AMG)':
        #         i[7]= 'INTER UNIT'
                print('yes')
            else:
        #         i[7]= 'INDIRECT EXPORT'
                print('three')
        else:
            pass
    else:
        pass


# In[26]:


imp={}
for i in data[1:]:
#     print(i[4])
    if i[3]:
        imp[i[3]]=i[6]
    else:
        pass
print(imp)


# In[27]:


for i in data[1:]:
    if not i[6]:
        if i[3] in imp:
            i[6]= imp[i[3]]
        else:
            pass
    else: 
        pass
       # Iran, Islamic Republic of


# In[32]:


for i in data[1:]:
    print(i[23],i[6])
    if not i[23]:
        if i[6]=='INTERUNIT' or i[6]=='INTERUNIT':
            i[23]= 'PAKISTAN'
        else:
            pass
    else:
        pass
    


# In[34]:


for i in data[1:]:
#     i[23]=i[23].upper()
    print(i[23])


# In[35]:


a= pd.DataFrame(data)


# In[36]:


a.head(10)


# In[37]:


header= a.iloc[0]
a=a[1:]
# a.reset_index(drop=True)
# a.columns = header
a=a.rename(columns= header )


# In[38]:


a.head(10)


# In[39]:


a.to_csv('final_sales.csv')


# In[40]:


a['FANCYNAME'].value_counts()


# In[47]:


a[(a['COUNTRY'] != 'PAKISTAN') and (a['CUSTOMER_TYPE'] == '')]


# In[46]:


a[a['CUSTOMER_TYPE'] == '']


# In[48]:


data1=list(reader(open('final_sales.csv', encoding='utf-8')))
data1


# In[49]:


data1[0].index('COUNTRY') 


# In[50]:


data1[0].index('CUSTOMER_TYPE')


# In[60]:


count=0
for i in data1[1:]:
    if not i[6]:
        if i[18] != 'PAKISTAN' and i[18]:
            i[6]= 'EXPORT'
#             print('sasaa')
#             print(i[18])

#             count +=1
        else:
            pass
    else:
        pass


# In[65]:


b= pd.DataFrame(data1)
header= b.iloc[0]
b=b[1:]
# a.reset_index(drop=True)
# a.columns = header
b=b.rename(columns= header )


# In[66]:


b.head(10)


# In[67]:


b[b['CUSTOMER_TYPE'] == '']


# In[68]:


b.to_csv('final_sales_file.csv')


# In[ ]:




