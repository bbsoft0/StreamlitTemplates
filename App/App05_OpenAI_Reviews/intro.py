import os
import streamlit as st
from openai import OpenAI

client = OpenAI()

st.header("Welcome to the OpenAI Chatbot")

reviews = st.text_area("Copy Paste any customer Review:")
button = st.button("Autoregenerate response")


def autoregenerate_response(reviews):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a customer service assistant, skilled in understanding and responding to customer reviews."},
            {"role": "user", "content": reviews}
        ]
    )
    return completion.choices[0].message

if reviews and button:
    with st.spinner("Generating response..."):
        reply = autoregenerate_response(reviews)
        st.text("Response:")
        st.write(reply.content)
