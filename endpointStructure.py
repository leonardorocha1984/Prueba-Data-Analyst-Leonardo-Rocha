# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
@author: win10
"""
from pydantic import BaseModel
# 2. Class that describes the fields of the endpoint
class EndpointFields(BaseModel):
    Income:float
    Kidhome:int
    Teenhome:int
    Recency:int
    MntWines:int
    MntFruits:int
    MntMeatProducts:int
    MntFishProducts:int
    MntSweetProducts:int
    MntGoldProds:int
    NumDealsPurchases:int
    NumWebPurchases:int
    NumCatalogPurchases:int
    NumStorePurchases:int
    NumWebVisitsMonth:int
    AcceptedCmp3:int
    AcceptedCmp4:int
    AcceptedCmp5:int
    AcceptedCmp1:int
    AcceptedCmp2:int
    Complain:int
    Z_CostContact:int
    Z_Revenue:int
    age:int
    Education_2n_Cycle:int
    Education_Basic:int
    Education_Graduation:int
    Education_Master:int
    Education_PhD:int
    Marital_Status_Absurd:int
    Marital_Status_Alone:int
    Marital_Status_Divorced:int
    Marital_Status_Married:int
    Marital_Status_Single:int
    Marital_Status_Together:int
    Marital_Status_Widow:int
    Marital_Status_YOLO:int

