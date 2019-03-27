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
u = "https://translate.google.co.in/#view=home&op=translate&sl=auto&tl=es&text="
f = u + t
print(f)


# In[11]:


import qrcode
img = qrcode.make(f)
img.show()


# In[ ]:




