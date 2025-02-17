import streamlit as st
import pandas as pd
import plotly.express as px
st.title('🎈 App Hakim')

st.write('Hello world!')


df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
with st.expander('data'):
  st.write("X")
  X_row = df.drop("species", axis=1)
  st.dataframe(X_row)
  st.write("y")
  y_row = df.species
  st.dataframe(y_row)
with st.sidebar:
  st.header("Признаки")
  island = st.selectbox("Island", ("Torgersen", "Dream", "Biscoe"))
  bill_length_mm = st.slider('Bill length(mm)', 32.1, 59.6, 44.5)
  bill_depth_mm = st.slider("bill_depth_(mm)", 13.1, 21.5, 17.3)
  flipper_length_mm = st.slider("flipper_length_mm", 32.1, 59.6, 44.5)
  body_mass_g = st.slider("body_mass_g", 32.1, 59.6, 44.5)
  gender = st.selectbox("gender", ("female", "male"))
st.subheader("data_vis")
fig  = px.scatter(
  df,
  x = 'bill_length_mm',
  y = 'bill_depth_mm',
  color='island')
st.plotly_chart(fig)
fig2 = px.histogram(
  df,
  x='body_mass_g',
  nbins=30)
st.plotly_chart(fig2)

import plotly.express as px

st.subheader('Data Visualization')
fig = px.scatter(
    df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='island',
    title='Bill Length vs. Bill Depth by Island'
)
st.plotly_chart(fig)

fig2 = px.histogram(
    df, 
    x='body_mass_g', 
    nbins=30, 
    title='Distribution of Body Mass'
)
st.plotly_chart(fig2)

data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'sex': gender
}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_raw], axis=0)
