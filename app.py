import pandas as pd
from flask import Flask,render_template, request, jsonify
#from Tensile_Strength.Stacking import preprocess
import numpy as np
import pickle

pipe= pickle.load(open('pipe.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict_strength():
    force= int(request.form.get('Force'))
    depth= float(request.form.get('Depth'))
    hole_radius=float(request.form.get('Hole Radius'))
    circle_radius=float(request.form.get('Circle Radius'))
    hole_angle=int(request.form.get('Hole Angle'))
    width= int (request.form.get('Width'))
    length=int(request.form.get('Length'))
    df= pd.DataFrame({'force':force,'depth':depth,'hole_radius':hole_radius,'circle_radius':circle_radius,
                      'hole_angle':hole_angle,'width':width,'length':length},index=[0])

    #print(df.shape)

    #prediction
    result =pipe.predict(df)[0]

    return render_template('index.html',result=result)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8080)


