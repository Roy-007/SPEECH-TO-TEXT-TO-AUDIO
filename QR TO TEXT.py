#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[2]:


r = sr.Recognizer()


# In[3]:


with sr.Microphone() as source:               
    audio = r.listen(source)  
    
t = r.recognize(audio)
print(t)


# In[4]:


import qrcode
img = qrcode.make(t)
img.show()


# In[ ]:




