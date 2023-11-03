from flask import Flask, render_template, request 
import numpy as np
import pickle
model= pickle.load(open('model (2).pkl', 'rb'))
app= Flask(__name__)
@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html')    
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/predict",methods=['GET','POST'])
def predict():
    return render_template('predict.html')
@app.route("/prediction",methods=['GET','POST'])    
def prediction():
    Administrative = request.form['Administrative']
    Administrative_Duration = request.form['Administrative_Duration']
    Informational= request.form['Informational']
    Informational_Duration = request.form['Informational_Duration']
    ProductRelated = request.form['ProductRelated']
    ProductRelated_Duration= request.form['ProductRelated_Duration']
    BounceRates = request.form['BounceRates']
    ExitRates = request.form['ExitRates']
    PageValues = request.form['PageValues']
    SpecialDay = request.form['SpecialDay']
    Month= request.form['Month']
    OperatingSystems = request.form['OperatingSystems']
    Browser = request.form['Browser']
    Region = request.form['Region']
    TrafficType = request.form['TrafficType']
    VisitorType = request.form['VisitorType']
    Weekend = request.form['Weekend']
    total = [[int (Administrative), float (Administrative_Duration), int(Informational), float(Informational_Duration), int (ProductRelated), float (ProductRelated_Duration), float (BounceRates), float (ExitRates), float(PageValues), float (SpecialDay), int (Month), int (OperatingSystems), int (Browser), int (Region), int(TrafficType), int (VisitorType), int (Weekend)]]
    print(total)
    prediction = model.predict(total)
    print (prediction)
    if prediction == 0:
       text = 'The visitor is not interested in buying products.'
    else:
        text = 'The visitor is interested in buying products'
    return render_template('submit.html', prediction_text=text)
    #return render_template('C:\\Users\\admin\\Desktop\\MINIPROJECT\\templates\\predict.html')
if __name__ =="__main__":
   app.run(debug=True)