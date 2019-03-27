#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio
import speech_recognition as sr


# In[2]:


r = sr.Recognizer()


# In[3]:




with sr.Microphone() as source:               
    audio = r.listen(source)  
    
print(r.recognize(audio));


# In[ ]:




