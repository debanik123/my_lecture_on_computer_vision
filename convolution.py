#!/usr/bin/env python
# coding: utf-8

# In[18]:


import cv2
import numpy as np

image  = cv2.imread("new.jpg")


# In[19]:


cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


filter_2d = np.ones((7,7),np.float32) / 9

operation =  cv2.filter2D(image,-1,filter_2d)
cv2.imshow("operation",operation)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[21]:


blur = cv2.blur(image,(3,3))
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


gaus = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("gaus",gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[23]:


median = cv2.medianBlur(image,5)
cv2.imshow("median",median)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[27]:


bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




