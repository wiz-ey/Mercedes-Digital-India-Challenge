from django.shortcuts import render
from .forms import CxForm
from .models import New
from.serializers import NewSerializer
from rest_framework import viewsets
from keras.models import load_model
import numpy as np
from django.contrib import messages
# Create your views here.
import tensorflow as tf
graph=tf.get_default_graph()
model = load_model('recommender/Mercedes-Benz.h5')

class NewView(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

def about_view(request):
    return render(request, 'recommender/about.html')

def form_view(request):
    if(request.method=='POST'):
        form = CxForm(request.POST)
        if(form.is_valid()):
            data = data_parser(request.POST)
            with graph.as_default():
                y = model.predict(data)
                # print(y[0][1])
                # print(y[1][1])
                a=np.sum(y[0],axis=0)
                b=np.sum(y[1],axis=0)
                a_max = np.amax(a)
                b_max = np.amax(b)
                a = list(a)
                b = list(b)

                print(a.index(a_max))
                print(b.index(b_max))
                messages.success(request, 'Finance Option : {}'.format(a.index(a_max)))
                messages.success(request, 'Car Model : {}'.format(b.index(b_max)))
                # print(np.amax(a))
                # print(np.amax(b))
                #l=np.array(y[0][2])
                #m=np.array(y[1][2])
                #print(np.where(np.amax(l)))
                #print(np.where(np.amax(m)))

            # res = form.save()
            # res.save()

            # unit = np.array(list(my_data.values()))
    else:
        form = CxForm()
    return render(request, 'recommender/getRecom.html', {'form':form})


def home_view(request):
    return render(request, 'recommender/base.html')

def data_parser(form_dict):
    form_list = [0,0,0,0,0,0,0,0,0,0]
    temp_list1 = []
    temp_list2 = []

    form_list[0] = (float(form_dict['credit_score']) - 700)/300
    form_list[1] = (float(form_dict['monthly_installment']) - 100000)/40000
    form_list[2] = (float(form_dict['maturity_day']) - 500)/300
    form_list[3] = (float(form_dict['outstanding_amt']) - 500000)/400000

    temp_list1 = form_dict['contract_status'].split(',')
    temp_list2 = form_dict['term_status'].split(',')

    for i in range(4,8):
        form_list[i] = int(temp_list1[i-4])

    for i in range(8,10):
        form_list[i] = int(temp_list2[i-8])
    data_list = []
    for i in range(10):
        data_list.append(form_list)

    data_list = np.array(data_list)

    return data_list
