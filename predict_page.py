# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:26:18 2022

@author: Lenovo
"""

import streamlit as st
import numpy as np
import pickle

def load_data():
    with open("D:\BIA\streamlit_Sir\saved_steps.pkl" , 'rb') as file:
        data = pickle.load(file)
        return data

data = load_data()

regressor_loaded = data["model"]
hours = data["hours"]

def show_predict_page():
    st.title("Students score prediction")
    st.write(""" ### WE need some information to predict the marks""")
    hrs = st.text_input("Enter number of hours you study : ","")
    
    ok = st.button("calculatemarks")
    if ok:
        X = np.array([[hrs]])
        X = X.astype(float)
       
        marks = regressor_loaded.predict(X)
        st.subheader(f"The estimated marks are {marks[0]:.2f}")
show_predict_page()