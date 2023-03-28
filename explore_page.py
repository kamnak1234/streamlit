# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:10:24 2022

@author: Lenovo
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def load_data():
    dataset = pd.read_csv("D:\BIA\streamlit_Sir\student_scores.csv")
    return dataset

def plot_hrs_scores():
    ds = load_data()
    fig = plt.figure(figsize = (10,5))
    plt.scatter('Hours','Scores' , data=ds)
    plt.title("Hours  vs Percentage")
    plt.xlabel('hours studied')
    plt.ylabel('percentage score')
    st.pyplot(fig)
    

def plot_bar():
    ds = load_data()
    fig1 = plt.figure(figsize=(10,5))
    plt.bar('Hours', 'Scores', color ='maroon',width = 0.4,data=ds)
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    st.pyplot(fig1)

def show_explore_page():
    st.title("Explore students study hours data")
    
    st.write(""" ### Studen study hours vs marks obtained """)
    plot_hrs_scores()
    plot_bar()

