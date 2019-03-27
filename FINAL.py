#!/usr/bin/env python
# coding: utf-8

# In[5]:


import speech_recognition as sr


# In[6]:


r = sr.Recognizer()


# In[7]:


with sr.Microphone() as source:               
    audio = r.listen(source)  
    
    
t = r.recognize(audio)
u = "https://translate.google.co.in/#view=home&op=translate&sl=auto&tl=es&text="
f = (u + t.replace(" ", "%20"))
print(f)


# In[8]:


import qrcode
img = qrcode.make(f)
img.show()


# In[ ]:




