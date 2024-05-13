#from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np
import cv2
from django.conf import settings
from django.shortcuts import render
import os

# Load the pre-trained model
model = load_model('/content/final-year-project/templates/cnnbtfinal_newest.h5')

# Mapping for class labels
class_labels = {0: 'glioma',
            1: 'meningioma',
            2: 'no tumor',
            3: 'pituitary',
            }

def classify_image(request):
    result = None
    img = None
    img1 = None
    if request.method == 'POST' and request.FILES['image']:
        
            img1 = request.FILES['image']
            temp_image_path = '/content/final-year-project/templates/temp_image.jpg'
            with open(temp_image_path, 'wb') as temp_file:
                for chunk in img1.chunks():
                    temp_file.write(chunk)
            img = cv2.imread(temp_image_path)
            #img = cv2.bilateralFilter(img, 2, 50, 50)
            #img = cv2.applyColorMap(img, cv2.COLORMAP_BONE)
            img = cv2.resize(img, (150, 150))
            img_array = np.array(img)
            #img_array = np.expand_dims(img_array, axis=0)
            #img_array = img_array / 255.0  # Normalize
            img_array = img_array.reshape(1,150,150,3)
            a=model.predict(img_array)
            indices = a.argmax()
            os.remove(temp_image_path)
            result = class_labels[indices]
           

        
            # Print the error for debugging
            

    return render(request, 'upload.html', {'result': result})
