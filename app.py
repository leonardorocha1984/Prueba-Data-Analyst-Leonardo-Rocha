# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020
@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from endpointStructure import EndpointFields
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model2.pkl","rb")
model=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_purchase(data:EndpointFields):
    data = data.dict()
    Income=data['Income']
    Kidhome=data['Kidhome']
    Teenhome=data['Teenhome']
    Recency=data['Recency']
    MntWines=data['MntWines']
    MntFruits=data['MntFruits']
    MntMeatProducts=data['MntMeatProducts']
    MntFishProducts=data['MntFishProducts']
    MntSweetProducts=data['MntSweetProducts']
    MntGoldProds=data['MntGoldProds']
    NumDealsPurchases=data['NumDealsPurchases']
    NumWebPurchases=data['NumWebPurchases']
    NumCatalogPurchases=data['NumCatalogPurchases']
    NumStorePurchases=data['NumStorePurchases']
    NumWebVisitsMonth=data['NumWebVisitsMonth']
    AcceptedCmp3=data['AcceptedCmp3']
    AcceptedCmp4=data['AcceptedCmp4']
    AcceptedCmp5=data['AcceptedCmp5']
    AcceptedCmp1=data['AcceptedCmp1']
    AcceptedCmp2=data['AcceptedCmp2']
    Complain=data['Complain']
    Z_CostContact=data['Z_CostContact']
    Z_Revenue=data['Z_Revenue']
    age=data['age']
    Education_2n_Cycle=data['Education_2n_Cycle']
    Education_Basic=data['Education_Basic']
    Education_Graduation=data['Education_Graduation']
    Education_Master=data['Education_Master']
    Education_PhD=data['Education_PhD']
    Marital_Status_Absurd=data['Marital_Status_Absurd']
    Marital_Status_Alone=data['Marital_Status_Alone']
    Marital_Status_Divorced=data['Marital_Status_Divorced']
    Marital_Status_Married=data['Marital_Status_Married']
    Marital_Status_Single=data['Marital_Status_Single']
    Marital_Status_Together=data['Marital_Status_Together']
    Marital_Status_Widow=data['Marital_Status_Widow']
    Marital_Status_YOLO=data['Marital_Status_YOLO']


    prediction = model.predict([[Income,Kidhome,Teenhome,Recency,MntWines,MntFruits,MntMeatProducts,MntFishProducts,MntSweetProducts,MntGoldProds,NumDealsPurchases,NumWebPurchases,NumCatalogPurchases,NumStorePurchases,NumWebVisitsMonth,AcceptedCmp3,AcceptedCmp4,AcceptedCmp5,AcceptedCmp1,AcceptedCmp2,Complain,Z_CostContact,Z_Revenue,age,Education_2n_Cycle,Education_Basic,Education_Graduation,Education_Master,Education_PhD,Marital_Status_Absurd,Marital_Status_Alone,Marital_Status_Divorced,Marital_Status_Married,Marital_Status_Single,Marital_Status_Together,Marital_Status_Widow,Marital_Status_YOLO]])
    if(prediction[0]==1):
        prediction="Comprara"
    else:
        prediction="No comprara"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
   