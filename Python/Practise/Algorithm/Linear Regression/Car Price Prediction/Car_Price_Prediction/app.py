from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler

import pickle

app=Flask(__name__)
#model=pickle.load(open('finalized_model_v1.pickle','rb'))



@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('index.html')


scaler=StandardScaler()
@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def predict():
    Fuel_Type_Diesel=0
    if request.method=='POST':
        Year = int(request.form['Year'])
        Year = 2020 - Year
        Year_scaled=scaler.fit_transform([[Year]])

        Present_Price=float(request.form['Present_Price'])
        Present_Price_scaled=scaler.fit_transform(([[Present_Price]]))


        Kms_Driven=int(request.form['Kms_Driven'])
        Kms_Driven_scaled=scaler.fit_transform([[Kms_Driven]])




        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if (Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif Fuel_Type_Petrol=='Diesel':
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0

        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if (Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0

        Transmission_Manual=request.form['Transmission_Manual']
        if Transmission_Manual=='Mannual':
            Transmission_Manual=1
        else:
            Transmission_Manual=0

        model = pickle.load(open('finalized_model_v1.pickle', 'rb'))
        #prediction = model.predict([[Present_Price_scaled, Kms_Driven_scaled, Year_scaled, Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        #prediction = model.predict([[Present_Price, Kms_Driven, Year, Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual, Transmission_Manual]])
        var = [Present_Price_scaled, Kms_Driven_scaled, Year_scaled, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
               Transmission_Manual]
        prediction = model.predict([var])
        output=round(prediction[0],2)
        print(var)

        print('prediction is', output)

        if output<0:
            return render_template('results.html',prediction='Sorry')
        else:
            return render_template('results.html',prediction=output)
    else:
        return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)

