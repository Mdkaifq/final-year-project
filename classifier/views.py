from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np
import cv2
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os


model = load_model('/content/final-year-project/templates/cnnbtfinal_newest.h5')


class_labels = {0: 'glioma',
            1: 'meningioma',
            2: 'no tumor',
            3: 'pituitary',
            }
@csrf_exempt
def classify_image(request):
    result = None
    img = None
    img1 = None
    if request.method == 'POST' and 'image' in request.FILES:
        
            img1 = request.FILES['image']
            temp_image_path = '/content/final-year-project/templates/temp_image.jpg'
            with open(temp_image_path, 'wb') as temp_file:
                for chunk in img1.chunks():
                    temp_file.write(chunk)
            img = cv2.imread(temp_image_path)
            img = cv2.resize(img, (150, 150))
            img_array = np.array(img)
            img_array = img_array.reshape(1,150,150,3)
            a=model.predict(img_array)
            indices = a.argmax()
            os.remove(temp_image_path)
            result = class_labels[indices]

    return render(request, 'imgclassifier.html', {'result': result})
