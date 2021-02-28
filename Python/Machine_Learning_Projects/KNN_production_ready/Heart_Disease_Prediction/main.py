from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler


import pickle
app=Flask(__name__)
scaler=StandardScaler()

@app.route("/",methods=['GET'])
def homepage():
    return render_template("Heart Disease Classifier.html")

@app.route("/predict",methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        try:
            age=int(request.form['age'])
            age_scaled=scaler.transform(age)

            sex=int(request.form['sex'])
            if sex==0:
                sex_1=0 #Female
            else:
                sex_1=1 #Male

            cp=int(request.form['cp'])
            if cp==1:
                cp_2,cp_3,cp_4=0,0,0
            elif cp==2:
                cp_2,cp_3,cp_4=1,0,0
            elif cp==3:
                cp_2, cp_3, cp_4 = 0, 1, 0
            else:
                cp_2, cp_3, cp_4 = 0, 0, 1


            trestbps=float(request.form['trestbps'])
            trestbps_scaled=scaler.transform(trestbps)

            chol=float(request.form['chol'])
            chol_scaled=scaler.transform(chol)

            fbs=int(request.form['fbs'])
            if fbs==0:
                fbs_1=0
            else:
                fbs_1=1

            restecg=int(request.form['restecg'])
            if restecg==0:
                restecg_1,restecg_2=0,0
            elif restecg==1:
                restecg_1,restecg_2=1,0
            else:
                restecg_1,restecg_2=0,1


            thalach=float(request.form['thalach'])
            thalach_scaled=scaler.transform(thalach)

            exang=float(request.form['exang'])
            if exang==0:
                exang_1=0
            else:
                exang_1=1

            oldpeak=int(request.form['oldpeak'])
            oldpeak_scaled=scaler.transform(oldpeak)

            slope=int(request.form['slope'])
            if slope==1:
                slope_2,slope_3=0,0
            elif slope==2:
                slope_2,slope_3=1,0
            else:
                slope_2, slope_3 = 0, 1

            ca=int(request.form['ca'])

            if ca==0:
                ca_1,ca_2,ca_3=0,0,0
            elif ca==1:
                ca_1, ca_2, ca_3 = 1, 0, 0
            elif ca==2:
                ca_1, ca_2, ca_3 = 0, 1, 0
            else:
                ca_1, ca_2, ca_3 = 0, 0, 1

            thal=int(request.form['thal'])
            if thal==3:
                thal_6,thal_7=0,0
            elif thal==6:
                thal_6,thal_7=1,0
            else:
                thal_6,thal_7=0,1

            print(age_scaled, trestbps_scaled, chol_scaled, thalach_scaled, oldpeak_scaled, sex_1,cp_2, cp_3, cp_4, fbs_1,
                                              restecg_1, restecg_2, exang_1,slope_2,slope_3,ca_1,ca_2,ca_3,thal_6,thal_7)


            filename="modelForPrediction.sav"
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[age_scaled, trestbps_scaled, chol_scaled, thalach_scaled, oldpeak_scaled, sex_1,cp_2, cp_3, cp_4, fbs_1,
                                              restecg_1, restecg_2, exang_1,slope_2,slope_3,ca_1,ca_2,ca_3,thal_6,thal_7]])
            print("Prediction is ",prediction[0])
            if prediction[0]==0:
                return render_template('result.html',result="No,Risk")
            else:
                return render_template('result.html',result="Yes,Risk")
        except Exception as e:
            print("The exception message is- ",e)
            return "something is wrong"
    else:
        return render_template('index.html')
app.run(debug=True)


