import streamlit as st
from aitextgen import aitextgen


st.title("AI TextGen App(Bala)")
# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
ai = aitextgen()

#prompt_text = "Machine Learning is awesome"
prompt_text = st.text_input(label="Enter input text",
              value="Machine learning is Beautiful")

with st.spinner("AI is on force........."):

    gpt_text = ai.generate_one(prompt=prompt_text,max_length=100)
#st.balloons()
st.success("Machine Learning Generated the text")
print(gpt_text)
st.text(gpt_text)