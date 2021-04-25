#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import os


# In[2]:


#creating an object for VGG16 model(pre-trained)

model = VGG16()


# In[3]:


model.summary()


# In[4]:


#Here we are taking sample images and predicting the same images on top of pre-trained VGG16 model.
#top=2 in decode_predictions() function means which we are taking top 2 probability values for the particular prediction. 

for file in os.listdir('sample'):
    print(file)
    full_path = 'sample/' + file
    
    image = load_img(full_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    y_pred = model.predict(image)
    label = decode_predictions(y_pred, top = 2)
    print(label)
    print()
    


# In[ ]:





# In[ ]:




