import streamlit as st
import pandas as pd
import csv as csv
import numpy as np
import pydeck as pdk
import random as rd
from PIL import Image

st.set_page_config(
    page_title="Home Page",
)
st.title("Strava Analyzer")
st.header('Welcome to the Website!')
st.write('The purpose of this website is to allow the user to upload their Strava data and then have it analyzed and then given back to the user in the form of both static and interactive graphs along with other interactive features, all to give insights to the end user in regard to the data that has been analyzed. Please note that in its current state, this website is in very early alpha, specifically alpha 0.05. in its current state, the website has very limited functionality, although, over the next couple of weeks, I plan to work on the website and, in doing so, increase its functionality and features substantially. This website for me is a passion project, and Im currently developing it on my own that being said, I would be more than happy to accept others who would be interested in developing it with me or have ideas for their website. if this sounds interesting or if you have ideas for features, dont hesitate to get in touch with me at cduval@falcon.bentley.edu')
st.header('How to Use the Website')
st.write('Listed below are step-by-step instructions on how use the website')
st.subheader('Step 1:')
st.image('pages/Steps/Step-1.png', caption='Log into Strava on the computer then go to the top right and click on settings',width=800)
st.subheader('Step 2:')
st.image('pages/Steps/Step-2.png', caption='Once in the settings menu, go over to the sidebar and click on the my account button',width=800)
st.subheader('Step 3:')
st.image('pages/Steps/Step-3.png', caption='Then once in the my account tab go down to the bottom of the page and click on get started under download or delete your account',width=800)
st.subheader('Step 4:')
st.image('pages/Steps/Step-4.png', caption='It will take you to this screen and then under download request click to request your archive',width=800)
st.subheader('Step 5:')
st.write('A little while later, you will receive an e-mail from Strava to the e-mail associated with that Strava account. this e-mail will contain a file that contains all of the information about your Strava account but to use this site the specific piece of information needed is an excel sheet that is with the file called activities.xlsx.')
st.subheader('Step 6:')
st.image('pages/Steps/Step-6.png', caption='Download the file and then open activities.xlsx then click on file once you have opened the excel sheet',width=800)
st.subheader('Step 7:')
st.image('pages/Steps/Step-7.png', caption='Once you have gotten to the file screen, click save as and then save a copy of the excel file as a CSV file to your computer. Once this step is completed, the new file should read activities.CSV',width=800)
st.subheader('Step 8:')
st.write('The final step is just to select/drag that file on the graphing tools page which will then analyze the file and display the results of that analysis')
