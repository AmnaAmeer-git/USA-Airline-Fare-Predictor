import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

import pickle
score = int

Year = ['1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
OriginCity = ['Los Angeles','Boston','New York City','Chicago','Dallas/Fort Worth','Houston','Cleveland','Miami','Atlanta','Detroit','Austin','Columbus','Charlotte','San Francisco','Kansas City','Albuquerque','Denver','Cincinnati','Las Vegas','Birmingham','Buffalo','Indianapolis','Jacksonville','Hartford','Phoenix','El Paso','Grand Rapids','Charleston','Memphis','Norfolk','Minneapolis/St. Paul','Nashville','Louisville','New Orleans','Dayton','Des Moines','Milwaukee','Fort Myers','Albany','Colorado Springs','Ltttle Rock','Boise','Portland','Greensboro/High Point','Knoxville','Madison','Greenville/Spartanburg','Orlando','Pittsburgh','Omaha','Raleigh/Durham','San Diego','Columbia','Eugene','San Antonio','Salt Lake City','Myrtle Beach','Oklahoma City','Burlington','Reno','Philadelphia','Fayetteville','Seattle','Rochester','St. Louis','Sacramento','Tampa','Syracuse','Amarillo','Huntsville','Corpus Christi','Washington','Daytona Beach','Pensacola','Tucson','Key West','Jackson/Vicksburg','Palm Springs','Savannah','Asheville','Atlantic City','Tulsa','Bozeman','Bellingham','Aspen','Harlingen/San Benito','Sarasota/Bradenton','Richmond','Melbourne','Bend/Redmond','Eagle','Baton Rouge','Jackson','Lexington','Tallahassee','Cedar Rapids/Iowa Ctiy','Flint','Nantucket','Valparaiso','Spokane','Fargo','Panama City','Everett','Allentown/Bethlehem/Easton','Gulfport/Biloxi','Fresno','Bangor',"Martha's Vineyard",'Harrisburg','Kalispell','Chattanooga','Bismarck/Mandan','Billings','Peoria','South Bend','Fort Wayne','Minot','Appleton','Charlottesville','Mobile','Springfield','Eureka/Arcata','Augusta','Pasco/Kennewick/Richland','Idaho Falls','Grand Forks','Medford','Concord','Missoula','Hilton Head','New Haven','Lansing','Montgomery','Latrobe','Bullhead City','Sioux Falls','Ashland','Fort Collins/Loveland','Belleville','Bloomington/Normal']
DestinationCity =  ['Los Angeles','Boston','New York City','Chicago','Dallas/Fort Worth','Houston','Cleveland','Miami','Atlanta','Detroit','Austin','Columbus','Charlotte','San Francisco','Kansas City','Albuquerque','Denver','Cincinnati','Las Vegas','Birmingham','Buffalo','Indianapolis','Jacksonville','Hartford','Phoenix','El Paso','Grand Rapids','Charleston','Memphis','Norfolk','Minneapolis/St. Paul','Nashville','Louisville','New Orleans','Dayton','Des Moines','Milwaukee','Fort Myers','Albany','Colorado Springs','Ltttle Rock','Boise','Portland','Greensboro/High Point','Knoxville','Madison','Greenville/Spartanburg','Orlando','Pittsburgh','Omaha','Raleigh/Durham','San Diego','Columbia','Eugene','San Antonio','Salt Lake City','Myrtle Beach','Oklahoma City','Burlington','Reno','Philadelphia','Fayetteville','Seattle','Rochester','St. Louis','Sacramento','Tampa','Syracuse','Amarillo','Huntsville','Corpus Christi','Washington','Daytona Beach','Pensacola','Tucson','Key West','Jackson/Vicksburg','Palm Springs','Savannah','Asheville','Atlantic City','Tulsa','Bozeman','Bellingham','Aspen','Harlingen/San Benito','Sarasota/Bradenton','Richmond','Melbourne','Bend/Redmond','Eagle','Baton Rouge','Jackson','Lexington','Tallahassee','Cedar Rapids/Iowa Ctiy','Flint','Nantucket','Valparaiso','Spokane','Fargo','Panama City','Everett','Allentown/Bethlehem/Easton','Gulfport/Biloxi','Fresno','Bangor',"Martha's Vineyard",'Harrisburg','Kalispell','Chattanooga','Bismarck/Mandan','Billings','Peoria','South Bend','Fort Wayne','Minot','Appleton','Charlottesville','Mobile','Springfield','Eureka/Arcata','Augusta','Pasco/Kennewick/Richland','Idaho Falls','Grand Forks','Medford','Concord','Missoula','Hilton Head','New Haven','Lansing','Montgomery','Latrobe','Bullhead City','Sioux Falls','Ashland','Fort Collins/Loveland','Belleville','Bloomington/Normal']

st.title('US Airline Fares Predictor')
pipe = pickle.load(open('myenv/London_AirlineFarePipeline.pkl', 'rb'))
model = pickle.load(open('myenv/USAirline_Fares.pkl', 'rb'))

col1,col2 = st.columns(2)

with col1:
    Year = st.selectbox('select the Year',sorted(Year))
with col2:
    quarter = st.number_input('quarter',step=1,format="%i")

col3,col4 = st.columns(2)

with col3:
    OriginCity = st.selectbox('select the Origin City',sorted(OriginCity))
with col4:
    DestinationCity = st.selectbox('select the Destination City',sorted(DestinationCity))

col5,col6 = st.columns(2)

with col5:
    Origin_Airport_ID = st.number_input('Origin Airport ID',step=1,format="%i")
with col6:
    Destination_Airport_ID = st.number_input('Destination Airport ID',step=1,format="%i")

col7,col8 = st.columns(2)

with col7:
    Distance_Btwn_Airport_Miles = st.number_input('Distance Between Airport Miles')
with col8:
    passengers = st.number_input('passengers',step=1,format="%i")

col9,col10 = st.columns(2)

with col9:
    large_ms = st.number_input('large ms')
with col10:
    largest_carrier_average_fare = st.number_input('largest carrier average fare')

if st.button('Predict Fare Prediction'):
    input_fare = pd.DataFrame({'Year':[Year],'quarter':[quarter],'OriginCity':[OriginCity],'DestinationCity':[DestinationCity],'Origin_Airport_ID':[Origin_Airport_ID],'Destination_Airport_ID':[Destination_Airport_ID],'Distance_Btwn_Airport_Miles':[Distance_Btwn_Airport_Miles],'passengers':[passengers],'large_ms':[large_ms],'largest_carrier_average_fare':[largest_carrier_average_fare]})

    result = pipe.predict(input_fare)
    st.text(result)