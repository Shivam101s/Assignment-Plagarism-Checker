
# coding: utf-8

# In[1]:


file1=open("doc1.txt","r")


# In[2]:


text1=file1.readlines()


# In[3]:


text1


# In[6]:


file2=open("doc2.txt","r")
text2=file2.readlines()
text2


# In[7]:


import nltk
str1=''.join(text1)
str2=''.join(text2)


# In[8]:


str1


# In[9]:


str2


# In[10]:


sent_text1=str1.split('.')


# In[11]:


sent_text2=str2.split('.')


# In[12]:


sent_text1


# In[13]:


sent_text2


# In[14]:


final_list=[]
for z in sent_text1:
    for y in sent_text2:
        if z == y:
            final_list.append(z)


# In[15]:


final_list

