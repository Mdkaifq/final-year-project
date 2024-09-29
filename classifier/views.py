from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np
import cv2
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os


#model = load_model('templates/cnnbtfinal_newest.h5')


class_labels = {0: 'glioma',
            1: 'meningioma',
            2: 'no tumor',
            3: 'pituitary',
            }
@csrf_exempt
def classify_image(request):
    result = None
    if request.method == 'POST' and 'image' in request.FILES:
        img1 = request.FILES['image']
        
        # Open the image directly from the uploaded file
        img_pil = Image.open(img1)

        # Convert the image to a format compatible with OpenCV
        img_cv = np.array(img_pil)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

        # Resize the image as per the model's requirements
        img_cv = cv2.resize(img_cv, (150, 150))

        # Convert image to numpy array and reshape for model input
        img_array = np.array(img_cv)
        img_array = img_array.reshape(1, 150, 150, 3)

        # Predict using the model
        a = model.predict(img_array)
        indices = a.argmax()

        # Get the classification result from labels
        result = class_labels[indices]
        
        return render(request, 'imgclassifier.html', {'result': result})
    
    return render(request, 'imgclassifier.html')

