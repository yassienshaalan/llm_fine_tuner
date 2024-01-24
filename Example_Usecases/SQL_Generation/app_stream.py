import streamlit as st
from transformers import pipeline

# Load your model
model_path = "path/to/your/model"
model = pipeline("text-generation", model=model_path)

st.title("SQL Generator")

# User input
input_text = st.text_input("Enter your text:")

if st.button("Generate SQL"):
    generated_sql = model(input_text)[0]['generated_text']
    st.text_area("Generated SQL:", value=generated_sql, height=300)
