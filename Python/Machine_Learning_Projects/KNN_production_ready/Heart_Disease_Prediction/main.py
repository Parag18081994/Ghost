from flask import Flask,request,render_template,Response
import pandas as pd


import pickle
app=Flask(__name__)
app.config['DEBUG'] = True


def predict_log(df):
    with open("standardScalar.sav",'rb') as f:
        scaler = pickle.load(f)
    col_scale=['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    df[col_scale] = scaler.transform(df[col_scale])
    print(df)
    with open("modelForPrediction.sav",'rb') as f:
        model=pickle.load(f)
    prediction=model.predict(df)
    if prediction[0] == 0:
        result = 'No,Risk'
    else :
        result = 'Yes,risk'
    return result


@app.route("/",methods=['GET'])
def homepage():
    return render_template("Heart Disease Classifier.html")

@app.route("/predict",methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        try:
            age=int(request.form['age'])
           

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
           

            chol=float(request.form['chol'])
           

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
           

            exang=float(request.form['exang'])
            if exang==0:
                exang_1=0
            else:
                exang_1=1

            oldpeak=float(request.form['oldpeak'])
           

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

           
            dic={'age':age,'trestbps': trestbps,'chol':chol,'thalach':thalach, 'oldpeak':oldpeak,"sex_1":sex_1,"cp_2":cp_2,"cp_3":cp_3,"cp_4":cp_4,"fbs_1":fbs_1,"restecg_1":restecg_1,"restecg_2":restecg_2,"exang_1":exang_1,"slope_2":slope_2,"slope_3":slope_3,"ca_1":ca_1 ,"ca_2":ca_2,"ca_3":ca_3,"thal_6":thal_6 ,"thal_7":thal_7}
            df_data=pd.DataFrame(dic,columns=['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex_1', 'cp_2', 'cp_3', 'cp_4', 'fbs_1','restecg_1','restecg_2','exang_1', 'slope_2', 'slope_3', 'ca_1', 'ca_2', 'ca_3', 'thal_6', 'thal_7'],index=[0])

            print(dic)
            prediction=predict_log(df_data)

            return render_template('Heart Disease Classifier.html',result=prediction)
        
        except ValueError:
            return Response("Value not found")
        except Exception as e:
            print('exception is   ',e)
            return Response(e)
    else:
        return render_template('Heart Disease Classifier.html')


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)



