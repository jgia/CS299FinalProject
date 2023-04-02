import streamlit as st
import pandas as pd
import csv as csv
import numpy as np
import pydeck as pdk
import random as rd
from PIL import Image
from matplotlib import pyplot as plt

st.set_page_config(
    page_title="Graphing Tools",
)
uploadedFile = st.file_uploader(label = '',type=['csv'],accept_multiple_files=False,key="fileUploader")
if uploadedFile is not None:
    df = pd.read_csv(uploadedFile)
    milelist = []
    kmlist = []
    actidlist = []
    totalmiles = []
    avgmileslist = []
    total = 0
    x = 1
    for row in df.Distance:
        if row == 0:
            milelist.append(0)
            kmlist.append(0)
            actidlist.append(x)
            total = total + row
            avgmiles = total/x
            avgmileslist.append(avgmiles)
            totalmiles.append(total)
        else:
            milelist.append(row/1.609)
            kmlist.append(row)
            actidlist.append(x)
            total = total + (row/1.609)
            avgmiles = total/x
            avgmileslist.append(avgmiles)
            totalmiles.append(total)

        x = x + 1
    df['Miles'] = milelist
    df['Kilometers'] = kmlist
    df['id'] = actidlist
    df['TotalMileage'] = totalmiles
    subframe = df[['id','Activity Date','Activity Name','Activity Type','Miles','Kilometers','Elapsed Time','Average Heart Rate','Max Heart Rate','Relative Effort','Moving Time','Max Speed','Average Speed','Elevation Gain','Elevation Loss','Elevation Low','Elevation High','Max Grade','TotalMileage']]
    subframe['avgmiles'] = avgmileslist
    with st.sidebar:
        options = st.selectbox(
        'What type of analysis would you like to do',
        ('Home', 'Graphs', 'Tables', 'Other-Charts'))
    if options == 'Home':
        st.header('Welcome')
        st.write('if you are reading this then you have successfully followed the instructions on the home page, and now your file has been analyzed. Currently, there are only so many features, but as the first test, I have made several graphs with the data you provided. You can see them by going to the sidebar and selecting the graphs tab.')
    if options == 'Graphs':
        mileper = subframe.loc[(subframe['Miles'] != 0),['id','Miles']]
        st.subheader('Miles Per Activity')
        fig2 = plt.figure(figsize=(15,8),linewidth=10)
        ax1 = fig2.add_axes([0.1,0.1,.8,0.8])
        plt.plot(mileper['id'],mileper['Miles'],color = 'red') # make a line
        plt.xlabel("Number of Activity")
        plt.ylabel("Number of Miles in Activity")
        st.pyplot(fig2)
        st.subheader('Average Miles Per Activity')
        fig4 = plt.figure(figsize=(15,8),linewidth=10)
        ax1 = fig4.add_axes([0.1,0.1,.8,0.8])
        plt.plot(subframe['id'],subframe['avgmiles'],color = 'green')
        plt.xlabel("Number of Activity's")
        plt.ylabel("Average Number of Miles")
        st.pyplot(fig4)
        st.subheader('Total Mileage')
        fig3 = plt.figure(figsize=(15,8),linewidth=10)
        ax2 = fig3.add_axes([0.1,0.1,.8,0.8])
        plt.plot(subframe['id'],subframe['TotalMileage'],color = 'red')  # make a line
        plt.xlabel("Number of Activity")
        plt.ylabel("Number of Miles")
        st.pyplot(fig3)
    if options == 'Tables':
        st.write('Under Construction')
    if options == 'Other-Charts':
        st.write('Under Construction')