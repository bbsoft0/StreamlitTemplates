import streamlit as st

st.markdown("## Image Embed Example")	
st.image("https://griddb-pro.azureedge.net/en/wp-content/uploads/2021/08/streamlit-1160x650.png") #method displays images.  st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("## Video Embed example ")	
st.video("https://www.youtube.com/watch?v=yG0RhKFTonw") # displays video. st.video(data, format="video/mp4", start_time=0) 

st.markdown("## Audio File Embed example")	
st.audio("https://bit.ly/rainaws3")   # displays audio.  st.audio(data, format="audio/wav", start_time=0)