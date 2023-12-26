import streamlit as st

st.title("Exploring Streamlit") # This is the first item of text our application will have. It’ll be displayed at the top of the application

st.header("Display Header") # for any major section of our application
st.subheader("Display Sub Header") #for smaller sections within each major section.

st.text("Display with st.text() ") # General text within our application body
st.markdown("`pip install streamlit` ") # For special formatting requirements

st.caption("Streamlit caption options") #  to display the captions of items displayed in our application.
st.write(" run Streamlit using the command `streamlit hello`") #will display whatever we specify in the parentheses based on the type of thing it is.

st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2") # Latex method to display mathematical equations.