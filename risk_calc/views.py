import pandas as pd
from django.shortcuts import render
from .models import predict
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def risk_calc(request):
    value_list = ['Age', 'Genetic Risk', 'Occupational Hazards', 'Headache',	'Seizure Rate',	'Convulsion Rate',	'Blurred Vision',	'Double Vision',	'Peripheral Vision Loss',	'Loss of Smell',	'Balance Disorder',	'Nausea',	'Vomiting',	'Rate of Memory Lapses',	'Drowsiness',	'Personality disorder',	'Numbness in arms',	'Numbness in legs',	'Syncope Rate'] # it will change every time view1 will get request
    pred = ['no risk detected', 'risk detected']
    df = None
    result = None
    if request.method == "POST":
        values_from_user = request.POST.getlist('my_list')
        #print(values_from_user)
        df = pd.DataFrame([values_from_user], columns=value_list)
        prediction = predict(df)
        result = pred[prediction[0]]
    return render (request, 'riskcalc.html', {'value_list': value_list, 'result':result})
