import streamlit as st
import numpy as np
import altair as alt
import matplotlib.pyplot as plt # External libraries 
import seaborn as sns
import pandas as pd 
import plotly.express as px
arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)


st.markdown("### MATPLOTLIB EXAMPLE") 
fig, ax = plt.subplots()
ax.set_title("Matplotlib Scatter Plot")
ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6) # Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
st.pyplot(fig) # Display a matplotlib.pyplot figure. 

st.markdown("### Seaborn EXAMPLE") 
fig, ax = plt.subplots()
ax.set_title("Seaborn Scatter Plot") 
ax = sns.scatterplot(arr1, arr2) # Seaborn is a library in Python predominantly used for making statistical graphics.
st.pyplot(fig)



st.markdown("### Altair Example")
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


arr1, arr2 = np.random.randn(100), np.random.rand(100)
arr3 = np.random.randint(1,1001,100)

fig = px.scatter(x=arr1, y=arr2, title="Plotly Scatter Plot")
st.plotly_chart(fig, use_container_width=True)
