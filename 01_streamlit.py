import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
	model="mixtral-8x7b-32768",
	temperature=0,
	groq_api_key = "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"

)

st.title("Simple LLM Chatbot")

st.write("Enter your query below:")
user_input = st.text_input("Your question :","")

if st.button("Get Answer"):
    response = llm.invoke(user_input)
    st.write("### Response:")
    st.write(response)