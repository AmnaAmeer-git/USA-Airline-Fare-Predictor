from flask import Flask, render_template, request
from jinja2 import Template
import numpy as np
import pandas as pd
import pickle
model= pickle.load(open('USAirline_Fares.pkl','rb'))
pipe = pickle.load(open('London_AirlineFarePipeline.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
    OriginCity= sorted(model['OriginCity'].unique())
    Year = sorted(model['Year'].unique(),reverse=True)
    DestinationCity= sorted(model['DestinationCity'].unique())

    return render_template('index1.html',OriginCity=OriginCity,Year=Year,DestinationCity=DestinationCity)

@app.route('/predict', methods=['GET','POST'])
def predict():

    OriginCity = request.form.get['OriginCity']
    Year = request.form.get['Year']
    DestinationCity = request.form.get['DestinationCity']
    quantity = int(request.form.get['quantity'])
    Origin_Airport_ID = int(request.form.get['Origin_Airport_ID'])
    Destination_Airport_ID = int(request.form.get['Destination_Airport_ID'])
    Distance_Btwn_Airport_Miles = int(request.form.get['Distance_Btwn_Airport_Miles'])
    passengers = int(request.form.get['passengers'])
    large_ms = int(request.form.get['large_ms'])
    largest_carrier_average_fare = int(request.form.get['largest_carrier_average_fare'])

    print(Year,quantity,OriginCity,DestinationCity,Origin_Airport_ID,Destination_Airport_ID,Distance_Btwn_Airport_Miles,passengers,large_ms,largest_carrier_average_fare)

    input = pd.DataFrame([[Year,quantity,OriginCity,DestinationCity,Origin_Airport_ID,Destination_Airport_ID,Distance_Btwn_Airport_Miles,passengers,large_ms,largest_carrier_average_fare]],columns=['Year','quantity','OriginCity','DestinationCity','Origin_Airport_ID','Destination_AAirport_ID','Distance_Btwn_Airport_Miles','passengers','large_ms','largest_carrier_average_fare'])

    prediction = pipe.predict(input)
    print(prediction)
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text='your pridicted value is {}'.format(output))
if __name__=="__main__":
    app.run(debug=True)
