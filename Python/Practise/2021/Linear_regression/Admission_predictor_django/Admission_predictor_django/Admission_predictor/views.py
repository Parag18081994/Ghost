from django.http import HttpResponse
from django.shortcuts import render
import pickle

def index(request):
    return render(request,'index.html')

def predict(request):
    gre_score= float(request.POST.get("gre_score"))
    toefl_score= float(request.POST.get("toefl_score"))
    university_rating= float(request.POST.get("university_rating"))
    sop_score= float(request.POST.get("sop_score"))
    lor_score= float(request.POST.get("lor_score"))
    cgpa= float(request.POST.get("cgpa"))
    research= request.POST.get("research")
    if research=='yes':
        research_val=1
    else:
        research_val=0
    print(gre_score, toefl_score, university_rating, sop_score, lor_score, cgpa, research_val)
    filename = 'Admission_prediction.pickle'
    loaded_model=pickle.load(open(filename,'rb'))
    prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop_score,lor_score,cgpa,research_val]])
    print(("Prediction-",prediction))


    return render(request,'predict.html')





