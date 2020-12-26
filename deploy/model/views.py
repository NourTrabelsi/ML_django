from django.shortcuts import render,HttpResponse
import joblib




def home(request):
    ##return HttpResponse('nour django')
    return render(request , 'home.html')

def result(request):
    prediction=joblib.load('IRIS_model.sav')
    x=[]
    x.append(request.GET['sepal_length'])
    x.append(request.GET['sepal_width'])
    x.append(request.GET['petal_length'])
    x.append(request.GET['petal_width'])


    res=prediction.predict([list(map(float,x))])
    a=int(res)
    result=""
    if a==0:
        result="Iris-setosa"
    elif a==1:
        result="Iris-versicolour"
    else:
        result="Iris-virginica"


    return render(request,'result.html',{'result':result})




