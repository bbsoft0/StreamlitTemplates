import streamlit as st
import numpy as np
import graphviz as graphviz
import pandas as pd 
df = np.random.randn(7,7)
st.markdown("## Displaying data we are using for charts ")
st.dataframe(df)
st.markdown("## Line Chart")
st.line_chart(df) # Display a line chart. 

st.markdown("## Area Chart")
st.area_chart(df) # Display an area chart 

st.markdown("## Bar Chart")
st.bar_chart(df)	  # Display a bar chart. 

st.markdown("## Gephaviz demo ")
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
    }
''') #Display a graph using the dagre-d3 library. 




st.markdown("## Map demo ")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df) # Display a map with points on it. 