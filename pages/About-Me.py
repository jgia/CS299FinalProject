import streamlit as st
import pandas as pd
import csv as csv
import numpy as np
import pydeck as pdk
import random as rd
from PIL import Image

st.set_page_config(
    page_title="About Me",
)
st.title('About Me')
st.image('pages/Steps/Image (4).jpeg',width=400)
st.header('My Background')
st.write('My name is Cole Duval. I’m currently 21 years old, and I currently go to Bentley university studying to get my undergraduate in computer information systems. I am on the cross-country team at Bentley, and I’m also in several clubs. I love getting outside and being active, and my favorite activities include running, coding, and playing the guitar.')
st.header('My Goals for this Website')
st.write('my short-term goals for this website are to increase its functionality and to add more features, my future plans for this website are two eventually add more robust features and to see how far I can go in terms of obtaining and analyzing data as well as potentially trying to add more interactive features such as and AI-driven race predictor.')
st.header('My Contact Information')
st.write('CellPhone Number:  1-413-209-1993')
st.write('Email:  Cduval@falcon.bentley.edu')