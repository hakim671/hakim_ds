import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
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
input_penguins = pd.concat([input_df, X_row], axis=0)

with st.expander("input_features"):
  st.dataframe(input_df)
  st.dataframe(input_penguins)
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
X = df_penguins[1:]
input_row = df_penguins[:1]
target_mapper = {'Adelie':0, 'Gentoo':2, 'Chinstrap':1}
def target_encode(val):
  return target_mapper[val]
y = y_row.apply(target_encode)
with st.expander("data preparation"):
  st.dataframe(input_row)
  st.write(y)
base_rf = RandomForestClassifier(random_state=42)
base_rf.fit(X, y)
pred = base_rf.predict(input_row)
pred_proba = base_rf.predict_proba(input_row)
df_pred_proba = pd.DataFrame(pred_proba, columns=['Adelie', 'Chinstrap', 'Gentoo'])

st.subheader('Predicted Species')
st.dataframe(
    df_pred_proba,
    column_config={
        'Adelie': st.column_config.ProgressColumn(
            'Adelie',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        ),
        'Chinstrap': st.column_config.ProgressColumn(
            'Chinstrap',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        ),
        'Gentoo': st.column_config.ProgressColumn(
            'Gentoo',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        ),
    },
    hide_index=True
)

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(f"Predicted species: **{penguins_species[pred][0]}**")
