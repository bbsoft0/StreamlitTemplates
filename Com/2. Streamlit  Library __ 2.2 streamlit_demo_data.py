import streamlit as st
import pandas as pd
import numpy as np 
st.markdown("### Metric Example ")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F") # Display a metric in big bold font, with an optional indicator of how the metric changed.

st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(label="Active developers", value=123, delta=-12,delta_color="off")

st.markdown("### JSON Example ")
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
}) # Display object or string as a pretty-printed JSON string. 


sample_data = {"Cities": ["New York", "San Jose", "Delhi","London","Berlin"]}
df = pd.DataFrame(sample_data)



st.markdown("### DataFrame Example ")
st.dataframe(df)  # Display a dataframe as an interactive table 


df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0)) # You can also pass a Pandas Styler object to change the style of the rendered DataFrame: 

st.markdown("### Table Example ")
st.table(df) # This differs from st.dataframe in that the table in this case is static: its entire contents are laid out directly on the page. 